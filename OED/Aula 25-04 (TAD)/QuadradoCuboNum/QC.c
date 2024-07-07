#include <stdio.h>
#include <stdlib.h>
#include "QC.h"

QuadradoCubo criarQuadradoCubo(float numero){
	QuadradoCubo qc;
	qc.numero = numero;

	return qc;
}

float calcularQuadrado(QuadradoCubo qc){
	return qc.numero * qc.numero;
}

float calcularCubo(QuadradoCubo qc){
	return qc.numero * qc.numero * qc.numero;
}
