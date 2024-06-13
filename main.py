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


@app.route('/home2')
def home2():
    return render_template('home2.html')

@app.route('/serviço')
def serviço():
    return render_template('servico.html')



@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/lista_agenda')
def lista_agenda():
    return render_template('lista_agenda.html', consultas=consultas)


@app.route('/verificar_agendamento', methods=['GET', 'POST'])
def verificar_agendamento():
    if request.method == 'POST':
        nome_animal = request.form['nome_animal']
        nome_tutor = request.form['nome_tutor']
        data = request.form['data']
        horario = request.form['horario']
        sintomas = request.form['sintomas']
        codigo = len(consultas)
        consultas.append([codigo, nome_animal, nome_tutor, data, horario,sintomas])
        return redirect('lista_agenda')
    else:
        return render_template('agendamento.html')


@app.route('/apagar_agendamento/<int:codigo>', methods=['GET', 'POST'])
def apagar_agendamento(codigo):
    del consultas[codigo]
    return redirect('/lista_agenda') # Redireciona de volta para a página inicial

@app.route('/paciente')
def paciente():
    return render_template('paciente.html')

@app.route('/verificar_paciente', methods=['GET', 'POST'])
def verificar_paciente():
    """
    Rota para adicionar um novo paciente.
    Se o método for POST, adiciona o novo paciente à lista.
    Se não, exibe o formulário para adicionar um novo paciente.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        especie = request.form['especie']
        peso = request.form['peso']
        nome_tutor1 = request.form['nome_tutor1']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nome, telefone, raca, peso, especie, nome_tutor1])
        return redirect('/home2')  # Redireciona para a página de usuário
    else:
        return render_template('paciente.html')  # Renderiza o formulário de adicionar paciente

# ABAIXO TEMOS O CÓDIGO DE EDIÇÃO DO PACIENTE:

@app.route('/editar_paciente/<int:codigo>', methods=['GET', 'POST'])
def editar_paciente(codigo):
    """
    Rota para editar um paciente existente.
    Se o método for POST, atualiza os detalhes do paciente com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do paciente para edição.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        especie = request.form['especie']
        peso = request.form['peso']
        nome_tutor1 = request.form['nome_tutor1']
        telefone = request.form['telefone']
        pacientes[codigo] = [codigo, nome, telefone, raca, peso, especie, nome_tutor1]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        paciente = pacientes[codigo]
        return render_template('editar_paciente.html', paciente=paciente)  # Renderiza o formulário de edição

@app.route('/apagar_paciente/<int:codigo>')
def apagar_paciente(codigo):
    del pacientes[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial



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

        return render_template('idadehumana.html', verificar_idadehumana = f'A idade humana aproximada do {especie2.lower()} é de aproximadamente {idade_humana} anos.')
    return render_template('idadehumana.html', verificar_idadehumana = '')



@app.route('/medicamentomg')
def medicamentomg():
    return render_template('medicamentomg.html')

@app.route('/verificar_medicamentomg', methods=['GET', 'POST'])
def verificar_medicamentomg():
    if request.method == 'POST':
        peso_animal1 = request.form['peso_animal1']
        doseremedio = int(request.form['doseremedio'])
        medicamentomg = (peso_animal1 * doseremedio)
        return render_template('medicamentomg.html', medicamentomg=medicamentomg)


@app.route('/desidratacao')
def desidratacao():
    return render_template('desidratacao.html')


@app.route('/verificar_quantidade_mililitros_soro/', methods=['POST'])
def verificar_quantidade_mililitros_soro():
        peso_animal = float(request.form['peso_animal'])
        grau_desidratacao = request.form['grau_desidratacao'].lower()

        if grau_desidratacao == 'leve':
            volume_fluidoterapia = 50 * peso_animal
        elif grau_desidratacao == 'moderada':
            volume_fluidoterapia = 75 * peso_animal
        elif grau_desidratacao == 'grave':
            volume_fluidoterapia = 100 * peso_animal
        else:
            return render_template('desidratacao.html', verificar_quantidade_mililitros_soro='Grau de desidratação inválido.')

        return render_template('desidratacao.html', verificar_quantidade_mililitros_soro=f'O grau de desidratação é {grau_desidratacao} e a fluidoterapia é de {volume_fluidoterapia} mL.')

if __name__ == '__main__':
    app.run(debug=True)