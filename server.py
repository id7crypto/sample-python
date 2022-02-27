import os
import datetime as dt
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
    
            filepath = os.path.join("/home/ADBot", "table.html")
            if not os.path.exists:
                print('table.html not found')
                self.send_response(400, message='table.html not found')
                return
    
            f = open(filepath, 'rb')
            t = dt.datetime.fromtimestamp(os.path.getmtime(filepath), tz=dt.timezone(dt.timedelta(hours=1)))
    
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(f"<html>{t.strftime('%Y-%m-%d %H:%M:%S %Z')}</html>\n".encode())
            self.wfile.write(f.read().strip())
            f.close()
        except Exception as e:
            print(e)
            self.send_response(400)


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % port)
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
