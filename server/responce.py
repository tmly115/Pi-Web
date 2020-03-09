
class Responce:



    def __init__(self, req):
        self.req = req


    def generate_responce(self, pages):

        if self.req.url in pages:
            body = pages[self.req.url]
            body_len = str(len(body))
            head = "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: " + body_len + "\n\n"
            responce = head + body
            return str(responce)
        else:
            return "HTTP/1.1 404\nContent-Type: text/html\nContent-Length: 27\n\n<h1>404 Page Not Found</h1>"
