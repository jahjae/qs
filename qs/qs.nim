import std/asynchttpserver
import std/asyncdispatch

proc main {.async.} =
  var server = newAsyncHttpServer()

  proc render(req: Request) {.async.} =
    echo (req.reqMethod, req.url, req.headers)
    echo req.url.path

    let headers = {"Content-type": "text/plain; charset=utf-8"}
    await req.respond(Http200, "Hello World", headers.newHttpHeaders())

  server.listen(Port(8000))
  let port = server.getPort
  echo "curl localhost:" & $port.uint16 & "/"
  
  while true:
    if server.shouldAcceptRequest():
      await server.acceptRequest(render)
    else:
      await sleepAsync(500)

waitFor main()


