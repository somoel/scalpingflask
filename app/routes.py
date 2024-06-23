from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome')
#
# @app.route('/alert/<int:id_signal>')
# def alert(id_signal):
#     # Aquí deberías obtener la señal correspondiente usando el id_signal
#     # y pasarla al template para mostrar la alerta
#     signal = get_signal_by_id(id_signal)
#     return render_template('alert.html', signal=signal)
#
# def reminder_signal_time(signal: IQSignal, id_signal: int) -> None:
#     """Function to warn with a window when the signal is two minutes away from starting."""
#     global current_windows
#     actual_sec = datetime.now().second
#     is_adjusted = False
#
#     while True:
#         current_time = datetime.now()
#         ctime_2min = current_time + timedelta(minutes=2)
#
#         if ctime_2min.hour == signal.time.hour and ctime_2min.minute == signal.time.minute:
#             winsound.PlaySound("src/notification_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
#             current_windows.append(AlertWindow(signal, id_signal))
#             current_windows[-1].fix_shown()
#             break
#
#         if not is_adjusted:
#             t.sleep(60 - actual_sec)
#             is_adjusted = True
#         else:
#             t.sleep(60)
#
# def get_signal_by_id(id_signal):
#     # Implementar lógica para obtener la señal por ID
#     pass
