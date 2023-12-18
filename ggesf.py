
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina.shaders import lit_with_shadows_shader


app = Ursina()
hand = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.gray, on_cooldown=False, rotation = (0, 0, 0))
sword = Entity(model="sword", parent=hand, position=(0, 0, 1), scale = 0.35, rotation = (0, 90, -8), texture = "Sword_texture")

random.seed(5)
Entity.default_shader=lit_with_shadows_shader
Entity(model='cube', y=1, shader=lit_with_shadows_shader)
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))

def change_voxel_textures(chosen):
    return textures[chosen]




class Bed(Button):
    def __init__(self, position=(0,0,0), texture="Bed"):
        super().__init__(parent=scene,
            position=position,
            model='Bed',
            origin_y=.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )




class Voxel(Button):
    textures = [
        "grass",
        "white_cube",
        "brick",
        
    ]

    def __init__(self, position=(0, 0, 0), texture=textures[0]):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            highlight_color=color.lime,
        )

    @staticmethod
    def texturing(key):
        try:
            index = int(key) - 1  
            if 0 <= index < len(Voxel.textures):
                return Voxel.textures[index]  
        except ValueError:
            pass 
        
for z in range(30):
    for x in range(30):
        for y in range(1):
            voxel = Voxel(position=(x,y,z))

bed = Bed(position=(4, 0.5, 4))        
bed = Bed(position=(26, 0.5, 26)) 


            

def input(key):
    if key.isdigit():  
        new_texture = Voxel.texturing(key)  
        if new_texture:  
            voxel.texture = new_texture  
    elif key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal, texture=voxel.texture)  
    elif key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

                
        

Sky()



player = FirstPersonController()
app.run()
