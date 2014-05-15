# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
<div class="primary-image">
  <img src="./static/stenosaurus-prototype.png" width="500px"/>
</div>
<form method="post" action="/signup" id="email-signup-form">
  <div id="signup-email">
    <input id="signup-email" maxlength="320" name="email" placeholder="Email address" type="email"/>
    <input id="source" name="source" type="hidden" value="prelaunch-splash-page"/>
    <button type="submit" class="signup-btn">Sign up to receive more details</button>
  </div>
</form>
