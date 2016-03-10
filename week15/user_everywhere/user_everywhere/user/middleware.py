class SetUserInRequestMiddleware:
    def process_request(self, request):
        print(request.user)
