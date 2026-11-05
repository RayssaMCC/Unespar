public class Calculadora {

	double valor_atual = 0;

	//soma
	double soma(double p1, double p2) {
		this.valor_atual = p1 + p2;
		return this.valor_atual;
	}
	
	double soma(double p) {
		this.valor_atual = this.valor_atual + p;
		return this.valor_atual;
	}


	//subtração
	double sub(double p1, double p2) {
		this.valor_atual = p1 - p2;
		return this.valor_atual;
	}
	
	double sub(double p) {
		this.valor_atual = this.valor_atual - p;
		return this.valor_atual;
	}


	//multiplicação
	double mult(double p1, double p2) {
		this.valor_atual = p1 * p2;
		return this.valor_atual;
	}
	
	double mult(double p) {
		this.valor_atual = this.valor_atual * p;
		return this.valor_atual;
	}


	//divisão
	double div(double p1, double p2) {
		this.valor_atual = p1 / p2;
		return this.valor_atual;
	}
	
	double div(double p) {
		this.valor_atual = this.valor_atual / p;
		return this.valor_atual;
	}


	//limpar
	void clean() {
		this.valor_atual = 0;
	}

}
