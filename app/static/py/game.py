import json

from browser import document, ajax

current_field = []
COLORS = {'A': '#c62828',
          'B': '#283593',
          'C': '#43a047',
          'D': '#f57c00',
          '0': '#aaaaaa'}

canvas = document['game']
ctx = canvas.getContext('2d')


def get_updates():
    pass


def init():
    def on_complete(request):
        print(request.responseText)
        data = json.loads(request.responseText)
        canvas.height = data['height'] * 15
        canvas.width = data['width'] * 15
        for i in range(len(data['field'])):
            for j in range(len(data['field'][i])):
                ctx.beginPath()
                ctx.rect(j * 15, i * 15, 15, 15)
                ctx.fillStyle = COLORS[data['field'][i][j]]
                print(COLORS[data['field'][i][j]])
                ctx.fill()
                ctx.beginPath()
                ctx.rect(j * 15, i * 15, 15, 15)
                ctx.stroke()

    print(1)
    req = ajax.Ajax()
    req.bind('complete', on_complete)
    req.open('POST', '/api/get_initial_config', True)
    req.send()

init()
