import http.server
import http.client
import json

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    EXPRESS_API_HOST = 'localhost'
    EXPRESS_API_PORT = 3000

    def do_GET(self):
        target_url = f'http://{self.EXPRESS_API_HOST}:{self.EXPRESS_API_PORT}{self.path}'

        try:
            api_connection = http.client.HTTPConnection(self.EXPRESS_API_HOST, self.EXPRESS_API_PORT)
            api_connection.request('GET', target_url)

            api_response = api_connection.getresponse()

            self.send_response(api_response.status)
            for header, value in api_response.getheaders():
                self.send_header(header, value)
            self.end_headers()

            response_content = api_response.read()
            self.wfile.write(response_content)

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

if __name__ == '__main__':
    proxy_host = 'localhost'
    proxy_port = 8080

    proxy_server = http.server.HTTPServer((proxy_host, proxy_port), ProxyHandler)
    print(f'Proxy server is running on http://{proxy_host}:{proxy_port}')

    try:
        proxy_server.serve_forever()
    except KeyboardInterrupt:
        print('\nProxy server stopped.')
