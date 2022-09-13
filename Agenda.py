import re,csv,itertools

class contacto:
    nuevo_id =itertools.count()
    def __init__(self,nombre,apellido,telefono):
        self.codigo = next(self.nuevo_id)
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        
    
class Agenda ():
    
    def __init__(self):
        self.contactos = []
    def appendd(self,nombre,apellido,telefono):
        contactoo = contacto(nombre,apellido,telefono)
        self.contactos.append(contactoo)
        
    def showall(self):
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
    
    def buscar(self,texto):
        encontrado = 0
        for contacto in self.contactos:
            if re.findall(texto,contacto.nombre) or re.findall(texto, contacto.apellido):
                self.imprimeContacto(contacto)
                encontrado = encontrado +1
        if encontrado == 0:
            self.noEncontrado()
            
    def borrar(self,codigo):
        
        for contacto in self.contactos:
            if contacto.codigo == codigo:
                
                print('----------------------------')
                print('Borrar el contacto? (si/no) ')
                print('----------------------------')
                opcion = str(input(">"))
                if opcion == 'si':
                    print('Contacto borrado')
                    del self.contactos[codigo]
                elif opcion == 'no':
                    break
    def grabar(self):
        with open ('agenda.csv','w') as fichero:
            escribir = csv.writer(fichero)
            escribir.writerow(('codigo','nombre','apellido','telefono'))
            for contacto in self.contactos:
                escribir.writerow((contacto.codigo,contacto.nombre,contacto.apellido,contacto.telefono))
    
    def imprimeContacto(self,contacto):
        print()
        print('------------------------------------------')
#        print('Codigo: {} '.format(contacto.codigo))
        print('Nombre: {} ' .format(contacto.nombre))
        print('Apellido: {} ' .format(contacto.apellido))
        print('Telefono: {} ' .format(contacto.telefono))
        print('------------------------------------------')
    def noEncontrado(self):
        print()
        print('------------------------------------------')
        print('Contacto no encontrado')
        print('------------------------------------------')
def ejecutar():
        global telefono
        agenda = Agenda()
        try:
            with open('agenda.csv','r') as fichero:
                lector =csv.DictReader(fichero,delimeter=',')
                for fila in lector:
                    agenda.add(fila['nombre'],fila['apellido'],fila['telefono'])
        except:
            print('Error al habrir el fichero')
        while True:
            Menu = str(input('''
                1.Mostrar lista de contactos \n
                2.Buscar contacto \n
                3.Add contacto \n
                4.Eliminar contacto \n
                5.Salir \n
                Elija una opcion escribiendo el numero: \n '''))
            
            if Menu == '1':
                agenda.showall()
            elif Menu == '2':
                texto = str(input('Escriba el nombre o apellido del contacto: '))
                agenda.buscar(texto.title())
            elif Menu == '3':
                nombre = str(input('Escribe el nombre: '))
                apellido = str(input('Escribe el apellido: '))
                movil = str(input('Escribe el telefono: '))
                agenda.appendd(nombre,apellido,movil)
                agenda.grabar()
            
            elif Menu == '4':
                contact = str(input('Escriba el Contacto a borrar: \n'))
                
                for contact in contacto.nuevo_id:
                    
                    agenda.buscar(str(contact))
                    print("Se eliminara: ",contact)
                    d = contact - 1
                    agenda.borrar(d)
                    
                    break
            elif Menu == '5':
                agenda.grabar()
                break
            else:
                print('Debe marcar una opcion del Menu')
if __name__=='__main__':
    ejecutar()
