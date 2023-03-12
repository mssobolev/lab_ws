from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import json


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if path == "/404":
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes('File Ne Naiden', "utf8"))  
        elif path == "/500":
            self.send_response(504)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes('Backend Server Error', "utf8"))  
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.send_header('AppName', 'python-web0.1')
            self.send_header('ServerID', 'Perviy')
            self.send_header('Set-Cookie', 'ws=abc1234567')
            self.end_headers()
            self.wfile.write(bytes('WEB -- 01', "utf8"))          
            self.wfile.write(bytes('<p>Method GET</p>', "utf8")) 
            self.wfile.write(bytes("<p>URL on server: " + self.path + "</p>", "utf8"))
            self.wfile.write(bytes("<p>REQ Headers: </p>" + str(self.headers) + "<p></p>", "utf8"))
            self.wfile.write(bytes("<p>SRC IP: " + self.client_address[0] + "</p>", "utf8"))

            path = self.path
            if path == "/red":
             file = open("pages"+path+".html", 'r')
            elif path == "/pic":
             file = open("pages/"+"1.svg")

            message = file.read()
            file.close()
            self.wfile.write(bytes(message, "utf8"))
            return
 

        

    def do_POST(self):
        self.send_response(200)
#        content.length = int(self.headers['Content-Length'])
        self.send_header('Content-type','text/json')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        messagep = "Method POST"
        self.wfile.write(bytes(messagep, "utf8"))
        self.wfile.write(bytes(self.headers))
        self.wfile.write(bytes(post_body))
        

def main():
    PORT = 80
    server = HTTPServer(('', PORT), echoHandler)
    print('Server running on port %s' %PORT)
    server.serve_forever()

if __name__== '__main__':
        main()
