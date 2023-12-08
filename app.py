from dash import Dash, html

# --------------------Aquí comienza la tarea--------------------

# Escribe tu nombre dentro de las comillas

mi_nombre = ''

# Guarda el fichero presionando ctrl + S

# --------------------Aquí termina la tarea---------------------

app = Dash(__name__)

app.layout = html.Div([
    html.H1(f'Hola {mi_nombre}', style={'color': 'white'}),
    html.H1("Te damos la bienvenida a The Bridge", style={'color': '#dd0b16'})
    ], style={
                'textAlign': 'center',
                'font-family': 'Lucida Console',
                'font-size': '1.5em',
                'position': 'absolute', 
                'top': '35%', 
                'left': '50%', 
                'transform': 
                'translate(-50%, -50%)', 
                'width': '70%',
                'background-color': '#080808', 
                'padding': '150px',
                'border': '10px solid #dd0b16'
    })

if __name__ == '__main__':
    app.run_server(port=80, debug=True)