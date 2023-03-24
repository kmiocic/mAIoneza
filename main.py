from init import *
import http.server
import socketserver

PORT = 5500

def main(): 
    

    ##Handler = http.server.SimpleHTTPRequestHandler

    ##with socketserver.TCPServer(("", PORT), Handler) as httpd:
    ##    print("serving at port", PORT)
    ##    httpd.serve_forever()

    init()

    





if __name__ == "__main__":
    main()

