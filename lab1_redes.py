import numpy as np
import matplotlib.pyplot as plot
from scipy.io import wavfile
from scipy.fftpack import fft as transformadaFourier
from scipy.fftpack import fftfreq as funcionFrecuencia
from scipy.fftpack import ifft as transformadaFourierInversa


# Se reconoce el archivo de audio handel y se guarda
# Donde datos es un arreglo que contiene las amplitudes
(espectro, datos) = wavfile.read('handel.wav')

# Se genera los valores de tiempo entre cada amplitud, Esto se hace especificamente para poner los parametros de numeros en el grafico. En el eje X
vectorTiempoAudio= np.linspace(0, len(datos)/espectro, num=len(datos))

# Se Configura y se plotea el grafico amplitud vs tiempo
"""plot.figure("Amplitud en el tiempo Original", [8.0, 4.5])
plot.title('Grafico: Audio original a través del tiempo')
plot.xlabel('Tiempo(en segundos)')
plot.ylabel('Amplitud')"""
#plot.plot(VectorTiempoAudio, datos)


#####################################################################################################################################
# TRANSFORMADA FOURIER

# Se obtiene la transformada de Fourier
DatosTransformadaFourier = transformadaFourier(datos)

# Se Calculan las frencuencias para Escalar en el eje X
frecuencias = funcionFrecuencia(len(datos), 1.0 /espectro)

# Se Configura y se plotea el grafico De la transformada de fourier de la señal en Dominio de la frecuencia
"""plot.figure("Señal en Dominio de la Frecuencia ", [9.0, 6.0])
plot.title('Grafico: Transformada de Fourier de la señal, en dominio de la frecuencia')
plot.xlabel('Frecuencia(Hz)')
plot.ylabel('Amplitud')
plot.plot(frecuencias, DatosTransformadaFourier)
plot.show()"""

#####################################################################################################################################
# TRANSFORMADA FOURIER INVERSA

# Calculo de la inversa de la transformada
datosTransformadaFourierInversa = transformadaFourierInversa(DatosTransformadaFourier)

# Se grafica la inversa de la transformada
plot.figure("Inversa de la Transformada", [9.0, 6.0])
plot.plot(vectorTiempoAudio, datosTransformadaFourierInversa)
plot.title('Grafico del audio con su transformada inversa en el tiempo')
plot.ylabel('Amplitud')
plot.xlabel('Tiempo (s)')

plot.show()

