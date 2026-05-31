def room_detail_en(request, room_name):
	room = next((r for r in ROOMS if r['slug'] == room_name), None)
	if not room:
		return render(request, 'cerinza/404.html', status=404)
	images = get_room_images(room['media_folder'], room.get('photos'))
	rooms = [{**r, 'images': []} for r in ROOMS]
	context = {
		'room': room,
		'images': images,
		'rooms': rooms,
		'spaces': SPACES,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/room_detail_en.html', context)
def space_detail_en(request, space_name):
	space = next((s for s in SPACES if s['slug'] == space_name), None)
	if not space:
		return render(request, 'cerinza/404.html', status=404)
	images = get_room_images(space['media_folder'], space.get('photos'))
	rooms = [{**r, 'images': []} for r in ROOMS]
	context = {
		'room': space,
		'images': images,
		'rooms': rooms,
		'spaces': SPACES,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/room_detail_en.html', context)
def english(request):
	rooms = []
	for room in ROOMS:
		images = get_room_images(room['media_folder'], room.get('photos'))
		rooms.append({**room, 'images': images[:3]})
	spaces = []
	for space in SPACES:
		images = get_room_images(space['media_folder'], space.get('photos'))
		spaces.append({**space, 'images': images[:3]})
	context = {
		'rooms': rooms,
		'spaces': spaces,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/english.html', context)
from django.shortcuts import render
import os
from django.conf import settings

ROOMS = [
	{
		'name': 'Laguna del alto',
		'name_en': 'Laguna del Alto',
		'slug': 'laguna-del-alto',
		'capacidad': 6,
		'descripcion': '2 camas dobles, 2 camas sencillas',
		'descripcion_en': '2 double beds, 2 single beds',
		'media_folder': 'laguna_del_alto',
		'photos': ['3.jpg', '1.jpg', '4.jpg', '11.jpg', '10.jpg', '12.jpg'],
		'detalle': 'La habitación Laguna del Alto rinde homenaje a uno de los parajes más emblemáticos de Cerinza. Ubicada en la vereda que lleva su nombre, esta zona es reconocida por su laguna de aguas cristalinas rodeada de montañas y frailejones. Es un destino ideal para los amantes de la naturaleza, el senderismo y la fotografía, donde se pueden observar aves endémicas y disfrutar de la tranquilidad de los paisajes andinos. Hospedarse aquí es sumergirse en la esencia natural y cultural de Cerinza.',
		'detalle_en': "The Laguna del Alto room pays tribute to one of Cerinza’s most emblematic places. Located in the namesake rural area, this zone is known for its crystal-clear lagoon surrounded by mountains and frailejones. It is an ideal destination for nature lovers, hiking, and photography, where you can spot endemic birds and enjoy the tranquility of the Andean landscapes. Staying here means immersing yourself in the natural and cultural essence of Cerinza."
	},
	{
		'name': 'Novare',
		'name_en': 'Novare',
		'slug': 'novare',
		'capacidad': 6,
		'descripcion': '1 cama doble, 2 camas semidobles',
		'descripcion_en': '1 double bed, 2 three-quarter beds',
		'media_folder': 'novare',
		'photos': ['11.jpg', '12.jpg', '10.jpg', '1.jpeg'],
		'detalle': 'La habitación Novare está inspirada en la vereda Novare, corazón agrícola de Cerinza. Sus campos fértiles y su gente laboriosa representan la tradición campesina del municipio. Aquí se cultivan productos típicos de la región y se vive la experiencia auténtica del campo boyacense, rodeado de montañas y aire puro. Es el lugar perfecto para quienes buscan conectar con la vida rural y la hospitalidad local.',
		'detalle_en': "The Novare room is inspired by the Novare rural area, the agricultural heart of Cerinza. Its fertile fields and hardworking people represent the farming tradition of the town. Here, typical regional products are grown and you can experience the authentic Boyacá countryside, surrounded by mountains and fresh air. It is perfect for those seeking to connect with rural life and local hospitality."
	},
	{
		'name': 'El Chital',
		'name_en': 'El Chital',
		'slug': 'el-chital',
		'capacidad': 4,
		'descripcion': '2 camas dobles',
		'descripcion_en': '2 double beds',
		'media_folder': 'el_chital',
		'photos': ['11.jpg', '12.jpg', '2.jpg', '10.jpg', '5.jpeg', '1.jpeg'],
		'detalle': 'El Chital es una vereda reconocida por sus senderos ecológicos y su ambiente apacible. La habitación que lleva su nombre invita a descubrir la riqueza natural de Cerinza, con paisajes de montaña, cultivos y la calidez de su gente. Es ideal para quienes desean explorar rutas rurales y disfrutar de la tranquilidad del entorno.',
		'detalle_en': "El Chital is a rural area known for its ecological trails and peaceful atmosphere. The room named after it invites you to discover Cerinza’s natural wealth, with mountain landscapes, crops, and the warmth of its people. It is ideal for those who want to explore rural routes and enjoy the tranquility of the surroundings."
	},
	{
		'name': 'El Tibet',
		'name_en': 'El Tibet',
		'slug': 'el-tibet',
		'capacidad': 4,
		'descripcion': '2 camas dobles',
		'descripcion_en': '2 double beds',
		'media_folder': 'el_tibet',
		'photos': ['10.jpg', '11.jpg', '2.jpg', '4.jpeg', '1.jpeg'],
		'detalle': 'La habitación El Tibet evoca la serenidad y belleza de la vereda homónima, un rincón de Cerinza donde el silencio y los paisajes verdes invitan al descanso. Es un espacio pensado para quienes buscan paz, meditación y contacto directo con la naturaleza.',
		'detalle_en': "The El Tibet room evokes the serenity and beauty of the rural area of the same name, a corner of Cerinza where silence and green landscapes invite you to rest. It is a space designed for those seeking peace, meditation, and direct contact with nature."
	},
	{
		'name': 'Martinez Peña',
		'name_en': 'Martinez Peña',
		'slug': 'martinez-pena',
		'capacidad': 2,
		'descripcion': '1 cama doble',
		'descripcion_en': '1 double bed',
		'media_folder': 'martinez_pena',
		'photos': ['1.jpg', '2.jpeg'],
		'detalle': 'Martínez Peña es una vereda de tradición campesina y vistas panorámicas. La habitación que lleva su nombre ofrece una experiencia íntima y acogedora, ideal para parejas o viajeros solitarios que desean disfrutar de la autenticidad y el paisaje rural de Cerinza.',
		'detalle_en': "Martinez Peña is a rural area with a farming tradition and panoramic views. The room named after it offers an intimate and cozy experience, ideal for couples or solo travelers who want to enjoy the authenticity and rural landscape of Cerinza."
	},
	{
		'name': 'Cobagote',
		'name_en': 'Cobagote',
		'slug': 'cobagote',
		'capacidad': 6,
		'descripcion': '2 camas dobles',
		'descripcion_en': '2 double beds',
		'media_folder': 'cobagote',
		'photos': ['1.jpg', '2.jpg', '3.jpg'],
		'detalle': 'La habitación Cobagote está dedicada a una de las veredas más tradicionales del municipio. Su ambiente rural, la cercanía a rutas ecológicas y la amabilidad de sus habitantes hacen de este lugar una opción perfecta para quienes buscan vivir la cultura y el paisaje boyacense.',
		'detalle_en': "The Cobagote room is dedicated to one of the most traditional rural areas of the town. Its rural atmosphere, proximity to ecological trails, and the friendliness of its inhabitants make this place a perfect option for those who want to experience Boyacá’s culture and landscape."
	},
]

SPACES = [
	{
		'name': 'Salón Boyacá',
		'name_en': 'Salón Boyacá',
		'slug': 'salon-boyaca',
		'capacidad': 30,
		'descripcion': 'Capacidad para 30 personas · Eventos',
		'descripcion_en': 'Capacity for 30 people · Events',
		'media_folder': 'salon_boyaca',
		'photos': ['14.jpg', '11.jpg', '10.jpg', '1.jpg', '15.jpg', '12.jpg', '13.jpg'],
		'detalle': 'El Salón Boyacá es un amplio espacio para eventos sociales y corporativos, con capacidad para hasta 30 personas. Ideal para reuniones, celebraciones, cumpleaños y eventos especiales en el corazón de Cerinza, Boyacá.',
		'detalle_en': 'Salón Boyacá is a spacious venue for social and corporate events, with capacity for up to 30 people. Ideal for meetings, celebrations, birthdays, and special events in the heart of Cerinza, Boyacá.',
	},
	{
		'name': 'Kiosko',
		'name_en': 'Kiosko',
		'slug': 'kiosko',
		'capacidad': 20,
		'descripcion': 'Capacidad para 20 personas · Eventos',
		'descripcion_en': 'Capacity for 20 people · Events',
		'media_folder': 'kiosko',
		'photos': ['4.jpg', '2.jpg', '3.jpg', '1.jpg'],
		'detalle': 'El Kiosko es un encantador espacio al aire libre con capacidad para 20 personas. Perfecto para reuniones informales, desayunos campestres y eventos al aire libre rodeados de la naturaleza boyacense.',
		'detalle_en': 'The Kiosko is a charming outdoor space with capacity for 20 people. Perfect for informal gatherings, countryside breakfasts, and outdoor events surrounded by Boyacá nature.',
	},
]

def get_room_images(folder, photos=None):
	media_path = os.path.join(settings.MEDIA_ROOT, folder)
	if not os.path.exists(media_path):
		return []
	if photos:
		return [
			os.path.join('media', folder, f) for f in photos
			if os.path.exists(os.path.join(media_path, f))
		]
	files = sorted([f for f in os.listdir(media_path) if f.lower().endswith(('jpg', 'jpeg', 'png'))])
	return [os.path.join('media', folder, f) for f in files]

def home(request):
	rooms = []
	for room in ROOMS:
		images = get_room_images(room['media_folder'], room.get('photos'))
		rooms.append({**room, 'images': images[:3]})
	spaces = []
	for space in SPACES:
		images = get_room_images(space['media_folder'], space.get('photos'))
		spaces.append({**space, 'images': images[:3]})
	context = {
		'rooms': rooms,
		'spaces': spaces,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/home.html', context)

def room_detail(request, room_name):
	room = next((r for r in ROOMS if r['slug'] == room_name), None)
	if not room:
		return render(request, 'cerinza/404.html', status=404)
	images = get_room_images(room['media_folder'], room.get('photos'))
	rooms = [{**r, 'images': []} for r in ROOMS]
	context = {
		'room': room,
		'images': images,
		'rooms': rooms,
		'spaces': SPACES,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/room_detail.html', context)

def space_detail(request, space_name):
	space = next((s for s in SPACES if s['slug'] == space_name), None)
	if not space:
		return render(request, 'cerinza/404.html', status=404)
	images = get_room_images(space['media_folder'], space.get('photos'))
	rooms = [{**r, 'images': []} for r in ROOMS]
	context = {
		'room': space,
		'images': images,
		'rooms': rooms,
		'spaces': SPACES,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/room_detail.html', context)
