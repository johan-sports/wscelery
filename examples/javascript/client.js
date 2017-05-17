window.onload = function() {
  function openSocket(taskId) {
    // Connect websocket
    var taskSocket = new WebSocket('ws://localhost:1337/' + taskId);

    $('p#status').text('Opened websocket, processing...');
    taskSocket.onmessage = function(event) {
      var msg = JSON.parse(event.data);

      switch(msg.type) {
      case 'task-succeeded':
        $('p#status').text('Task succeeded with result: ' + msg.result + ' Elapsed: ' + msg.runtime);
        taskSocket.close();
        break;
      case 'task-retried': // fallthrough
      case 'task-failed':
        $('p#status').text('Task failed with exception: ' + msg.exception);
        taskSocket.close();
        break;
      case 'task-rejected': // fallthrough
      case 'task-revoked':
        taskSocket.close();
        break;
      default: // ignore
        break;
      }
    };

    taskSocket.onerror = function() {
      $('p#status').text('Websocket error!');
    };
  }

  $('form#add').submit(function(event) {
    var formData = new FormData(event.target);
    var x = formData.get('x');
    var y = formData.get('y');
    // Create task
    $.ajax({
      url: 'http://localhost:5000/add/' + x + '/' + y,
      type: 'POST',
      success: function(data) {
        $('p#status').text('Received task with ID:', data.task_id);
        openSocket(data.task_id);
      },
      error: function() {
        $('p#status').text('Request to web API failed.');
      }
    });
    event.preventDefault();
  });
};
