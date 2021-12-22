from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        masukr = int(request.POST['r'])
        masukt = int(request.POST['t'])
        keluar = (1/3)*(22/7)*(masukr^2)*masukt
        context = {'keluar': keluar,
                   }
        return render(request, 'main/home.html', context)

    else:
        return render(request, 'main/home.html', {})