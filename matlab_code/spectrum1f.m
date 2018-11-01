function a=spectrum1f(NN,plotflag)

%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% 1/f exponente Compute.
%
% USE:
%	a=spectrum1f(NN,plotflag)
%
%
% INPUT: 
%       .-NN ---> Time series.
%       .-plotflag ---> Plot (flag=1) the estimate procedure.
% OUTPUT: 
%       .-a ---> Scaling exponent.
%       
%        
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% AUTHORS:
%
% José Luis Rojo Álvarez
% Óscar Barquero Pérez
% Rebeca Goya Esteban
% 
% DATE: 18-10-2007
%
% VERSION 1.0

if nargin < 2
    plotflag = 0;
end

NN=NN(:)-mean(NN);

% Danger with prime factor of fft
while 1
   if length(factor(length(NN)))<3,
      NN=NN(1:end-1);
   else
      break
   end
end

l=length(NN);
fs=1;
f=fs/l*(0:l-1);
ini=min(find(f>=1e-4));
fin=min(find(f>=1e-2));

X=abs(fft(NN)).^2;
Xvlf=X(ini:fin);
ff=f(ini:fin);

[a,b]=myregress(log(ff),log(Xvlf));

if plotflag,
    figure
    plot(log(ff),log(Xvlf),'b',...
        log(ff),a*log(ff)+b,'r');
    xlabel('log(Hz)');
    ylabel('log(ms^2)');
    axis tight
    
    %se indica en la grafica la pendiente
    texto = sprintf('%s %1.2f',texlabel('alpha ='),a);
    %h=gtext(texto);
    ejes = axis;
    text(ejes(1)+.7*(ejes(2)-ejes(1)),ejes(3)+.85*(ejes(4)-ejes(3)),texto);
end

% Bands for freq
endulf=min(find(f>.003));
endvlf=min(find(f>.04));
endlf=min(find(f>.15));
endhf=min(find(f>.40));
endvhf=min(find(f>.50));
tot=sum(X(1:endvhf));
pulf=sum(X(1:endulf-1))/tot*100;
pvlf=sum(X(endulf:endvlf-1))/tot*100;
plf=sum(X(endvlf:endlf-1))/tot*100;
phf=sum(X(endlf:endhf-1))/tot*100;
pvhf=sum(X(endhf:endvhf))/tot*100;


function [a,b]=myregress(x,y)

%
x=x(:);y=y(:);

A=[sum(x.^2),sum(x);
   sum(x),length(x)];
C=[sum(x.*y);sum(y)];
v=inv(A)*C;
a=v(1); b=v(2);
