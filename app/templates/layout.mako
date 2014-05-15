# -*- coding: utf-8 -*- 
<!DOCTYPE html>  
<html>
<head>
  <meta charset="utf-8">
  <title>Stenosaurus</title>
  <meta name="author" content="Open Steno Project">
  <link rel="shortcut icon" href="/static/favicon.ico">
  <link rel="stylesheet" href="/static/style.css">
</head>

<body>
  <div id="splash-logo">
    <a href="/"><img src="./static/stenosaurus-logo.png" width="240px"/></a>
  </div>
  <p class="splash-heading">Stenography is about to evolve.</p>

  % if request.session.peek_flash():
  <div id="flash">
    <% flash = request.session.pop_flash() %>
	% for message in flash:
	${message}<br>
	% endfor
  </div>
  % endif

  <div id="page">
    ${next.body()}
  </div>
  
</body>
</html>
