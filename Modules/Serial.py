import serial
from threading import Thread
from queue import Queue

class SerialComunication:
    def __init__(self):
        self.printer = serial.Serial('/dev/ttyACM0',115200,timeout=None)
        self.software = serial.Serial('/dev/tnt1',115200,timeout=None)
        self.thread_PS = Thread(target=ser.sniff_printer_software)
        self.thread_SP = Thread(target=ser.sniff_software_printer)
        self.queue = Queue()

    def sniff_software_printer(self):
        while True:
            line = self.software.readline()
            self.queue.put(line)
            self.printer.write(line)

    def sniff_printer_software(self):
        while True:
            line = self.printer.readline()
            self.queue.put(line)
            self.software.write(line)


if __name__ == "__main__":
    ser = SerialComunication()

    ser.thread_PS.start()
    ser.thread_SP.start()

    comand_list = []

    while len(comand_list)<50:
        if not ser.queue.empty():
            comand = ser.queue.get()
            if comand.startswith(b'T') or comand.startswith(b'M'):
                print(comand)
                comand_list.append(comand)

    print(comand_list)




