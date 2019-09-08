import numpy as np
import matplotlib.pyplot as plot
from scipy.io import wavfile
from scipy.fftpack import fft as transformadaFourier
from scipy.fftpack import fftfreq as funcionFrecuencia
from scipy.fftpack import ifft as transformadaFourierInversa

################ LECTURA DEL AUDIO HANDEL.WAV  ##################################################################################
# Se reconoce el archivo de audio handel y se guarda, Donde datos es un arreglo que contiene las amplitudes
(freqMuestreo, datos) = wavfile.read('handel.wav')


##################################### PLOTEO DE LECTURA HANDEL ##################################################################
def graficoSenalHandel(freqMuestreo,datos):

    # Se genera los valores de tiempo entre cada amplitud, Esto se hace especificamente para poner los parametros de numeros en el grafico. En el eje X
    vectorTiempoAudio= np.linspace(0, len(datos)/freqMuestreo, num=len(datos))

    # Se Configura y se plotea el grafico amplitud vs tiempo
    plot.figure("Amplitud en el tiempo Original", [8.0, 4.5])
    plot.title('Grafico: Audio original a través del tiempo')
    plot.xlabel('Tiempo(en segundos)')
    plot.ylabel('Amplitud')
    plot.plot(vectorTiempoAudio, datos)

    return 0

#################################   TRANSFORMADA FOURIER    #####################################################################
def transformadaFourierYgrafico(freqMuestreo,datos):

    datosTransformadaFourier = transformadaFourier(datos)   # Se obtiene la transformada de Fourier
    print(datosTransformadaFourier)
    frecuencias = funcionFrecuencia(len(datos), 1.0 /freqMuestreo) # Se Calculan las frencuencias para Escalar en el eje X

    # Se Configura y se plotea el grafico De la transformada de fourier
    plot.figure("Señal en Dominio de la Frecuencia ", [9.0, 6.0])
    plot.title('Grafico: Transformada de Fourier de la señal, en dominio de la frecuencia')
    plot.xlabel('Frecuencia(Hz)')
    plot.ylabel('Amplitud')
    plot.plot(frecuencias, datosTransformadaFourier)
    plot.show()

    return datosTransformadaFourier

###############################  TRANSFORMADA FOURIER INVERSA  ##################################################################
def transformadaFourierInversaYgrafico(datosTransformadaFourier,freqMuestreo,datos):

    datosTransformadaFourierInversa = transformadaFourierInversa(datosTransformadaFourier) # Calculo de la inversa de la transformada
    vectorTiempoAudio = np.linspace(0, len(datos) / freqMuestreo, num=len(datos))

    # Se grafica la inversa de la transformada
    plot.figure("Inversa de la Transformada", [9.0, 6.0])
    plot.plot(vectorTiempoAudio, datosTransformadaFourierInversa)
    plot.title('Grafico del audio con su transformada inversa en el tiempo')
    plot.ylabel('Amplitud')
    plot.xlabel('Tiempo (s)')

    plot.show()

    return 0




############################ BLOQUE PRINCIPAL O MAIN ################################

graficoSenalHandel(freqMuestreo,datos)
a = transformadaFourierYgrafico(freqMuestreo,datos)
transformadaFourierInversaYgrafico(a,freqMuestreo,datos)