def english(request):
	rooms = []
	for room in ROOMS:
		images = get_room_images(room['media_folder'])
		rooms.append({**room, 'images': images[:3]})
	context = {
		'rooms': rooms,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/english.html', context)
from django.shortcuts import render
import os
from django.conf import settings

ROOMS = [
	{
		'name': 'Laguna del alto',
		'slug': 'laguna-del-alto',
		'capacidad': 6,
		'descripcion': '2 camas dobles, 2 camas sencillas',
		'media_folder': 'Laguna del alto',
		'detalle': 'La habitación Laguna del Alto rinde homenaje a uno de los parajes más emblemáticos de Cerinza. Ubicada en la vereda que lleva su nombre, esta zona es reconocida por su laguna de aguas cristalinas rodeada de montañas y frailejones. Es un destino ideal para los amantes de la naturaleza, el senderismo y la fotografía, donde se pueden observar aves endémicas y disfrutar de la tranquilidad de los paisajes andinos. Hospedarse aquí es sumergirse en la esencia natural y cultural de Cerinza.'
	},
	{
		'name': 'Novare',
		'slug': 'novare',
		'capacidad': 6,
		'descripcion': '1 cama doble, 2 camas semidobles',
		'media_folder': 'Novare',
		'detalle': 'La habitación Novare está inspirada en la vereda Novare, corazón agrícola de Cerinza. Sus campos fértiles y su gente laboriosa representan la tradición campesina del municipio. Aquí se cultivan productos típicos de la región y se vive la experiencia auténtica del campo boyacense, rodeado de montañas y aire puro. Es el lugar perfecto para quienes buscan conectar con la vida rural y la hospitalidad local.'
	},
	{
		'name': 'El Chital',
		'slug': 'el-chital',
		'capacidad': 4,
		'descripcion': '2 camas dobles',
		'media_folder': 'El Chital',
		'detalle': 'El Chital es una vereda reconocida por sus senderos ecológicos y su ambiente apacible. La habitación que lleva su nombre invita a descubrir la riqueza natural de Cerinza, con paisajes de montaña, cultivos y la calidez de su gente. Es ideal para quienes desean explorar rutas rurales y disfrutar de la tranquilidad del entorno.'
	},
	{
		'name': 'El Tibet',
		'slug': 'el-tibet',
		'capacidad': 4,
		'descripcion': '2 camas dobles',
		'media_folder': 'El Tibet',
		'detalle': 'La habitación El Tibet evoca la serenidad y belleza de la vereda homónima, un rincón de Cerinza donde el silencio y los paisajes verdes invitan al descanso. Es un espacio pensado para quienes buscan paz, meditación y contacto directo con la naturaleza.'
	},
	{
		'name': 'Martinez Peña',
		'slug': 'martinez-pena',
		'capacidad': 2,
		'descripcion': '1 cama doble',
		'media_folder': 'Martinez Peña',
		'detalle': 'Martínez Peña es una vereda de tradición campesina y vistas panorámicas. La habitación que lleva su nombre ofrece una experiencia íntima y acogedora, ideal para parejas o viajeros solitarios que desean disfrutar de la autenticidad y el paisaje rural de Cerinza.'
	},
	{
		'name': 'Cobagote',
		'slug': 'cobagote',
		'capacidad': 6,
		'descripcion': '2 camas dobles',
		'media_folder': 'Cobagote',
		'detalle': 'La habitación Cobagote está dedicada a una de las veredas más tradicionales del municipio. Su ambiente rural, la cercanía a rutas ecológicas y la amabilidad de sus habitantes hacen de este lugar una opción perfecta para quienes buscan vivir la cultura y el paisaje boyacense.'
	},
]

def get_room_images(folder):
	media_path = os.path.join(settings.MEDIA_ROOT, folder)
	if not os.path.exists(media_path):
		return []
	files = [f for f in os.listdir(media_path) if f.lower().endswith(('jpg', 'jpeg', 'png'))]
	return [os.path.join('media', folder, f) for f in files]

def home(request):
	rooms = []
	for room in ROOMS:
		images = get_room_images(room['media_folder'])
		rooms.append({**room, 'images': images[:3]})
	context = {
		'rooms': rooms,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/home.html', context)

def room_detail(request, room_name):
	room = next((r for r in ROOMS if r['slug'] == room_name), None)
	if not room:
		return render(request, 'cerinza/404.html', status=404)
	images = get_room_images(room['media_folder'])
	context = {
		'room': room,
		'images': images,
		'logo': os.path.join('media', 'logo.png'),
	}
	return render(request, 'cerinza/room_detail.html', context)
