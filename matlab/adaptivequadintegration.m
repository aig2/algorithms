%Trapezoid rule - Adaptive quadrature
%The program takes in the function f, endpoints and the tolerance tol
% that the program needs to fullfill and runs recursively if the tolerance is
%too big for as many times as needed
%Usage: [y,nrbil]=v2h1a(f,a,b,tol)
%before: The function f, interval [a,b] and the tolerance tol are known.
%after: The function f has been intergrated over the interval [a,b] numerically
%.      using the trapezoid rule / adaptive quadrature

function [y,nrbil]=v2h1a(f,a,b,tol)
	global finalTol;
	x=linspace(a,b,500);
	plot(x,f(x),'r')
	legend('y =1+exp(sin(x)) ')
	xlabel('X')
	ylabel('Y')
	hold on
	fa=f(a);
	fb=f(b);
	Tab=((fa+fb)/2)*(b-a);
	global nrb;
	nrb=0;
	y=adtrap(f,f(a),f(b),Tab,a,b,tol);
	%nrb er fjöldi keyrslna sem forritið stendur upp með að keyra með
	%tilliti til nákvæmni (tol) semkrafist er
	fprintf('Number of subintervals are %d',nrb/2)
	fyrirprintf('Number of total runs are %d for the tolerance %.5f',nrb,tol)
	fprintf('\nThe approximation of the integral using the trapezoid rule provides %.5f',y);
	nrbil=nrb;
end

function y=adtrap(f,fa,fb,Tab,a,b,tol)
	global nrb
	global finalTol
	c=(a+b)/2;
	fc=f(c);
	%Tab=(fa+fb)/2*(b-a);
	Tac=(fa+fc)/2*(c-a);
	Tcb=(fc+fb)/2*(b-c);
	%skekkju yrðing
	if abs(Tab-(Tac+Tcb))<=3*tol
		%talningabreytan nrb hækkar um 2 fyrir hverja ítrun sem þarf að gera
		%vegna þess að þá þarf að reikna fyrir tvö bil í stað eins.
		nrb=nrb+2;
		y=(Tac+Tcb);
		%plottaðar beinar línur til að afmarka trapisu bil á myndinni sem
		%heildað er í raun yfir til að nálga heildið á f(x)
		x=linspace(a,b,50);
		p=@(x) fa*((b-x)/(b-a))+fb*((x-a)/(b-a));
		line([a a], [0 fa]);
		plot(x,p(x))
	else
		y=adtrap(f,fa,fc,Tac,a,c,tol/2)+adtrap(f,fc,fb,Tcb,c,b,tol/2);
    end
end








end
end