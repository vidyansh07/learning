from http.server import HTTPServer, BaseHTTPRequestHandler
import time


HOST = '192.168.172.87'
PORT_NUMBER = 8000

class NuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", 'utf-8'))

    # def do_POST(self):
    #     self.send_response(200)
    #     self.send_header('Content-type', 'application/json')
    #     self.end_headers()
    #     date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    #     self.wfile.write(bytes('{"time : "'+ date + '"}', "utf-8"))
        
    
    
if __name__ == '__main__':
    server_address = (HOST, PORT_NUMBER)
    print('Starting')
    server = HTTPServer(server_address, NuralHTTP)
    server.serve_forever()
    server.server_close()
    print('Finished')
    