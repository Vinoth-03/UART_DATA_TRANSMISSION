import serial
import time


arduino_port = 'COM8'
baud_rate = 2400


serial_connection = serial.Serial(arduino_port, baud_rate)
time.sleep(2)


Info = "Finance Minister Arun Jaitley criticized former RBI governor Raghuram Rajan for suggesting that the next banking crisis could arise from MSME lending, arguing that hindsight is always clearer than foresight. Rajan, who previously served as the chief economist at the IMF and had forewarned the 2008 financial crisis, cautioned against ambitious credit targets and loan waivers in a note to a parliamentary committee. He warned that they might precipitate the next banking crisis. The government should not only address the last crisis but also anticipate the sources of the next one. It should exercise restraint in setting ambitious credit targets or forgiving loans, as meeting such targets can sometimes involve bypassing proper due diligence, thereby paving the way for future NPAs. Rajan also suggested a closer scrutiny of both MUDRA loans and the Kisan Credit Card, as these popular schemes may harbor potential credit risks. Rajan, who served as the RBI governor for three years until September 2016, is currently."

print("Transmission from PC to MCU")


initial_time = time.time()
total_bytes_sent = 0


for byte in Info.encode('utf-8'):
    serial_connection.write(bytes([byte]))
    current_time=time.time()

    
    if initial_time != current_time:
        transmission_rate =  8 /(current_time - initial_time)
        print(f"Transmission Rate: {transmission_rate: } bits/second")

print("Completed!!!.\n")
time.sleep(2)


serial_connection.write(b"0\n1005\n")


no_of_char = 0

received_data = ""
print("Reception from MCU")

initial_time = time.time()

while True:
    if serial_connection.in_waiting > 0:
        received_byte = serial_connection.read(serial_connection.in_waiting)
        data = received_byte.decode('utf-8',errors='replace')
        received_data += data
        no_of_char += len(received_data)
        current_time = time.time()
        

        
        if  current_time != initial_time:
            reception_rate = no_of_char * 8 / (current_time-initial_time)
            print(f"Reception Rate: {reception_rate:.2f} Received: {data} bits/second")
        total_bytes_received = 0
        initial_time = time.time()

        
        if len(received_data) >= len(Info.encode('utf-8')):
            break

received_text = received_data.strip()

print("\nReceived Data:\n")
print(received_text)
print("\nReception complete.\n")


serial_connection.close()
