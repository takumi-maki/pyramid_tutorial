from pyramid.view import view_config, view_defaults


@view_defaults(route_name='hello')
class TutorialViews:
    def __init__(self, request) -> None:
        self.request = request
        self.view_name = 'TutorialViews'

    @property
    def full_name(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return first + ' ' + last

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        return {'page_title': 'Home View'}

    @view_config(renderer='hello.pt')
    def hello(self):
        return {'page_title': 'Hello View'}

    @view_config(route_name='think', renderer='think.pt')
    def think(self):
        return { 'page_title': 'Think View'}

    @view_config(request_method='POST', renderer='edit.pt')
    def edit(self):
        new_name = self.request.params['new_name']
        return {'page_title': 'Edit View', 'new_name': new_name}

    @view_config(request_method='POST', request_param='form.delete', renderer='delete.pt')
    def delete(self):
        print('Deleted')
        return {'page_title': 'Delete View'}
