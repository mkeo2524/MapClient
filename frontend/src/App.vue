<template>
  <div id='app'>
    <title>Upload new File Test</title>
    <h1>Upload new File</h1>
      <form method=post action="http://127.0.0.1:5000/upload" enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h1>Marker Set Get API Test</h1>
    <form method=get action="http://127.0.0.1:5000/get">
      <input type=submit value=Submit>
    </form>
  </div>

</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
