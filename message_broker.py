import uuid

class ColaDinamica:
  """
  Clase que representa una cola dinámica similar a una cola de RabbitMQ.

  Atributos:
    mensajes (dict): Un diccionario que almacena los mensajes en la cola.
    id_cola (str): Un identificador único para la cola.
  """

  def __init__(self):
    self.mensajes = {}
    self.id_cola = str(uuid.uuid4())

  def publicar(self, mensaje):
    """
    Agrega un mensaje a la cola.

    Argumentos:
      mensaje (str): El mensaje a agregar.
    """
    self.mensajes[str(uuid.uuid4())] = mensaje

  def consumir(self):
    """
    Obtiene y elimina el siguiente mensaje de la cola.

    Retorna:
      str: El mensaje obtenido, o None si la cola está vacía.
    """
    if not self.mensajes:
      return None

    mensaje_id, mensaje = next(iter(self.mensajes.items()))
    del self.mensajes[mensaje_id]
    return mensaje

# Ejemplo de uso
cola_ejemplo = ColaDinamica()

cola_ejemplo.publicar("Este es un mensaje de prueba")
cola_ejemplo.publicar("Otro mensaje de prueba")
cola_ejemplo.publicar("Otro mensaje de prueba")
cola_ejemplo.publicar("Otro mensaje de prueba")
cola_ejemplo.publicar("Otro mensaje de prueba")
cola_ejemplo.publicar("Otro mensaje de prueba")
cola_ejemplo.publicar("Otro mensaje de prueba")
cola_ejemplo.publicar("Otro mensaje de prueba")


while True:
    mensaje_recibido = cola_ejemplo.consumir()
    if mensaje_recibido is None:
        break
    print(f"Mensaje recibido: {mensaje_recibido}") # Mensaje None, la cola está vacía
