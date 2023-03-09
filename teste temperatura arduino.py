import serial
import random
import datetime

class Boiler:
    def __init__(self, name):
        self.name = name
        self.temperature = 0
        self.pressure = 0
        self.last_temperature = 0
        self.last_pressure = 0
        
    def update_temperature(self):
        # Simula a leitura de temperatura da caldeira
        self.last_temperature = self.temperature
        self.temperature = random.uniform(200, 300)
        
    def update_pressure(self):
        # Simula a leitura de pressão da caldeira
        self.last_pressure = self.pressure
        self.pressure = random.uniform(10, 15)
        
class ColdRoom:
    def __init__(self, name):
        self.name = name
        self.temperature = 0
        self.last_temperature = 0
        
    def update_temperature(self):
        # Simula a leitura de temperatura da câmara fria
        self.last_temperature = self.temperature
        self.temperature = random.uniform(-10, 5)
        
class MonitoringSystem:
    def __init__(self, boilers, cold_rooms, arduino_port):
        self.boilers = boilers
        self.cold_rooms = cold_rooms
        self.report = []
        
        # Configuração da comunicação serial com o Arduino
        self.arduino_port = arduino_port
        self.serial_connection = serial.Serial(arduino_port, 9600)
        
    def update_readings(self):
        # Atualiza as leituras de temperatura e pressão
        for boiler in self.boilers:
            boiler.update_temperature()
            boiler.update_pressure()
            # Envia as leituras da caldeira para o Arduino via comunicação serial
            self.serial_connection.write(f'{boiler.temperature:.2f},{boiler.pressure:.2f}'.encode())
            
        for cold_room in self.cold_rooms:
            cold_room.update_temperature()
            # Envia as leituras da câmara fria para o Arduino via comunicação serial
            self.serial_connection.write(f'{cold_room.temperature:.2f}'.encode())
        
    def generate_report(self):
        # Gera um relatório das variações de temperatura e pressão
        report_time = datetime.datetime.now()
        report = f'Relatório de Monitoramento - {report_time}\n\n'
        
        for boiler in self.boilers:
            temperature_variation = boiler.temperature - boiler.last_temperature
            pressure_variation = boiler.pressure - boiler.last_pressure
            
            report += f'Caldeira {boiler.name}:\n'
            report += f'Temperatura: {boiler.temperature:.2f}ºC (variação de {temperature_variation:.2f}ºC)\n'
            report += f'Pressão: {boiler.pressure:.2f} psi (variação de {pressure_variation:.2f} psi)\n\n'
        
        for cold_room in self.cold_rooms:
            temperature_variation = cold_room.temperature - cold_room.last_temperature
            
            report += f'Câmara Fria {cold_room.name}:\n'
            report += f'Temperatura: {cold_room.temperature:.2f}ºC (variação de {temperature_variation:.2f}ºC)\n\n'
        
        self.report.append(report)
        
        # Envia o relatório para o Arduino via comunicação serial
