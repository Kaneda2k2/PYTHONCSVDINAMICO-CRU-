#create and read from a csv file
import csv



def create_csv_file():
    records= [
        {'id':'1','cif':'numero','deudor':'nombre','nombrejuez':'nombre','nombrejuzgado':'nombrejuzgado','numerojuzgado':'numero','procedimiento':'numero','mediador':'nombre','contenidoedicto':'contenido'},
    ]   
    csv_writer = csv.writer(open('record.csv','w'), delimiter=',')
    csv_writer.writerow(['Id','Cif','Deudor','Nombrejuez','Nombrejuzgado','Numerojuzgado','Procedmiento','Mediador','Contenidoedicto'])
    for record in records:
         csv_writer.writerow([record['id'],record['cif'],record['deudor'],record['nombrejuez'],record['nombrejuzgado'],record['numerojuzgado'],record['procedimiento'],record['mediador'],record['contenidoedicto']])


def read_csv_file():
    for row in csv.reader(open('record.csv','r'), delimiter=','):
        if len(row) > 0:
            print(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6]+' '+row[7]+' '+row[8])


def update_csv_file():
    csv_writer = csv.writer(open('record.csv','a'), delimiter=',')
    csv_writer.writerow(['2','4906665','Clesa','Nombrejuez','Nombrejuzgado','Numerojuzgado','Procedmiento','Mediador','Contenidoedicto'])

if __name__ == "__main__":
    #create_csv_file()
    #read_csv_file()
    #update_csv_file()

