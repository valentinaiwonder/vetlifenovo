from flask import Flask, render_template, request, redirect
app = Flask(__name__)

consultas = []
pacientes = []

@app.route('/')
def index():
    return render_template('index.html', pacientes=pacientes, consultas= consultas)


@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/serviço')
def serviço():
    return render_template('servico.html')



@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/verificar_agendamento', methods=['GET', 'POST'])
def verificar_agendamento():
    if request.method == 'POST':
        nome_animal = request.form['nome_animal']
        nome_tutor = request.form['nome_tutor']
        data = request.form['data']
        horario = request.form['horario']
        codigo = len(consultas)
        consultas.append([codigo, nome_animal, nome_tutor, data, horario,])
        return redirect('/')
    else:
        return render_template('agendamento.html')

@app.route('/apagar_consulta')
def apagar_consulta():
    return render_template('agendamento.html')

@app.route('/verificar_apagar_consulta/<int:codigo>')
def verificar_apagar_consulta(codigo):
    del consultas[codigo]
    return redirect('/index.html/') # Redireciona de volta para a página inicial

@app.route('/paciente')
def paciente():
    return render_template('paciente.html')

@app.route('/verificar_paciente', methods=['GET', 'POST'])
def verificar_paciente():

    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        especie = request.form['especie']
        peso = request.form['peso']
        nome_tutor1 = request.form['nome_tutor1']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nome, telefone, raca, peso, especie, nome_tutor1])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('paciente.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar_paciente')
def editar_paciente():
    return render_template('editar_paciente.html')

@app.route('/verificar_editar_paciente/<int:codigo>', methods=['GET', 'POST'])
def verificar_editar_paciente(codigo):

    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        especie = request.form['especie']
        peso = request.form['peso']
        nome_tutor1 = request.form['nome_tutor1']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nome, telefone, raca, peso, especie, nome_tutor1])
        return redirect('/')  # Redireciona de volta para a página inicial

    else:
        contato = pacientes[codigo]
        return render_template('editar_paciente.html', contato=contato)  # Renderiza o formulário de edição



@app.route('/idadehumana')
def idadehumana():
    return render_template('idadehumana.html', verificar_idadehumana='')

@app.route('/verificar_idadehumana', methods=['GET', 'POST'])
def verificar_idadehumana():
    if request.method == 'POST':
        especie2 = request.form['especie2']
        idade2 = int(request.form['idade2'])

        if especie2.lower() == 'cachorro':
            if idade2 == 1:
                idade_humana = 15
            elif idade2 == 2:
                idade_humana = 24
            elif idade2 == 3:
                idade_humana = 28
            elif idade2 == 4:
                idade_humana = 32
            elif idade2 == 5:
                idade_humana = 36
            elif idade2 == 6:
                idade_humana = 40
            elif idade2 == 7:
                idade_humana = 44
            else:
                idade_humana = 44 + (idade2 - 7) * 5

        elif especie2.lower() == 'gato':
            if idade2 == 1:
                idade_humana = 15
            elif idade2 == 2:
                idade_humana = 24
            elif idade2 == 3:
                idade_humana = 28
            elif idade2 == 4:
                idade_humana = 32
            elif idade2 == 5:
                idade_humana = 36
            else:
                idade_humana = 36 + (idade2 - 5) * 4

        return render_template('idadehumana.html', verificar_idadehumana = f'A idade humana aproximada do {especie.lower()} é de aproximadamente {idade_humana} anos.')
    return render_template('idadehumana.html', verificar_idadehumana = '')



@app.route('/medicamento_mg')
def medicamento_mg():
    return render_template('medicamento_.html')

@app.route('/verificar_medicamento_mg', methods=['GET', 'POST'])
def verificar_medicamento_mg():
    if request.method == 'POST':
        peso = request.form['peso']
        doseremedio = int(request.form['doseremedio'])
        medicamento_mg = (peso * doseremedio)
        return render_template('medicamento_mg.html', medicamento_mg=medicamento_mg)

@app.route('/desidratacao')
def desidratacao():
    return render_template('desidratacao.html')


@app.route('/verificar_quantidade_mililitros_soro/', methods=['POST'])
def verificar_quantidade_mililitros_soro():

    peso_animal = float(request.form['peso_animal'])
    grau_desidatracao = request.form['grau_desidatracao']
    if grau_desidatracao.lower() == 'leve':
        volume_fluidoterapia = 50 * peso_animal
    elif grau_desidatracao.lower() == 'moderada':
        volume_fluidoterapia = 75 * peso_animal
    elif grau_desidatracao.lower() == 'grave':
        volume_fluidoterapia = 100 * peso_animal

    return render_template('desidratacao.html')

if __name__ == '__main__':
    app.run(debug=True)