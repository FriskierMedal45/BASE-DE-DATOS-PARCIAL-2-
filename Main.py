import redis
import json
import time

#CONEXIÓN A LA NUBE 
r = redis.Redis(
    host='gentle-kite-176177.upstash.io',
    port=6379,
    password='gQAAAAAAArAxAAIgcDE1NTYxN2ZjMTUzZmI0MTY1YTNhZDk4NDA4ZDdmMDdmOQ',
    ssl=True, 
    decode_responses=True 
)

# --- OPERACIONES CRUD ---

def crear_carrito(user_id, items):
    key = f"cart:{user_id}"
    r.hset(key, mapping={"items": json.dumps(items), "status": "activo"})
    
    # REQUISITO: Consulta Especializada -> Patrón TTL (Time To Live)
    r.expire(key, 1800)
    print(f"[CREATE] Carrito creado para {user_id}. Expirará en 30 minutos.")

def leer_carrito(user_id):
    key = f"cart:{user_id}"
    if r.exists(key):
        cart = r.hgetall(key)
        cart['items'] = json.loads(cart['items']) # Parseamos el JSON
        print(f"[READ] Carrito de {user_id}: {cart}")
        return cart
    print(f"[READ] El carrito de {user_id} no existe o ya expiró.")
    return None

def actualizar_carrito(user_id, nuevos_items):
    key = f"cart:{user_id}"
    if r.exists(key):
        r.hset(key, "items", json.dumps(nuevos_items))
        r.expire(key, 1800) 
        print(f"[UPDATE] Carrito de {user_id} actualizado. TTL reiniciado.")
    else:
        print(f"[UPDATE] Error: El carrito no existe.")

def eliminar_carrito(user_id):
    key = f"cart:{user_id}"
    r.delete(key)
    print(f"[DELETE] Carrito de {user_id} eliminado exitosamente (Checkout completado).")

# --- SCRIPT DE PRUEBA (Seeding y Demostración) ---
if __name__ == "__main__":
    print("--- INICIANDO DEMOSTRACIÓN CRUD Y TTL EN REDIS ---")
    usuario = "user_9981"
    
    # 1. CREATE
    crear_carrito(usuario, [{"producto": "Monitor 4K", "precio": 350, "cant": 1}])
    
    # 2. READ
    leer_carrito(usuario)
    
    # 3. UPDATE
    actualizar_carrito(usuario, [
        {"producto": "Monitor 4K", "precio": 350, "cant": 1},
        {"producto": "Cable HDMI", "precio": 15, "cant": 2}
    ])
    leer_carrito(usuario)
    
    # 4. DEMOSTRACIÓN
    tiempo_restante = r.ttl(f"cart:{usuario}")
    print(f"[INFO] Tiempo de vida restante del carrito: {tiempo_restante} segundos")
    
    # 5. DELETE
    eliminar_carrito(usuario)
    leer_carrito(usuario)