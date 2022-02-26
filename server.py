import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
    
            filepath = os.path.join("/home/ADBot", "table.html")
            if not os.path.exists:
                print('table.html not found')
    
            f = open(filepath, 'rb')
    
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(f.read().strip())
            f.close()
        except Exception as e:
            print(e)
            self.send_response(400)
#    def do_GET(self):
#        self.send_response(HTTPStatus.OK)
#        self.end_headers()
#        dirs = os.listdir("/home/")
#        msg = 'Hello! you requested %s' % (self.path)
#        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
