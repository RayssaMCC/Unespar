#ifndef QC_H_INCLUDED
#define QC_H_INCLUDED

typedef struct {
	float numero;
} QuadradoCubo;

QuadradoCubo criarQuadradoCubo(float numero);
float calcularQuadrado (QuadradoCubo qc);
float calcularCubo (QuadradoCubo qc);

#endif //QC_H_INCLUDED
