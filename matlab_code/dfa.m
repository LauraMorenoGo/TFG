function [alpha] = dfa(rr,flag)
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% Hurst exponent estimated by the DFA method.
%
% USE:
%	[alpha] = dfa(rr,flag)
%
% INPUT: 
%       .-rr ---> Time series.
%       .-flag ---> Plot (flag=1) the estimate procedure.
% OUTPUT: 
%       .-alpha  ---> Scaling exponent, realted with the Hurst exponent by 
%        H = alpha + 1.
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% AUTHORS:
% REBECA GOYA ESTEBAN
% OSCAR BARQUERO PEREZ
% 
% DATE: 18-10-2007
%
% VERSION 1.0

if nargin<2
    flag = 0;
end
rr = rr(:);
rr = rr';
rr = rr - mean(rr);
y = cumsum(rr); %Integration
L = length(y);
%Segementation 
npuntos = 80;
n = round(logspace(log10(3),log10(length(rr)/4),npuntos) );
%n(64) = 100; %Para pintar ejemplo real con 1000 muestras. En otro caso comentar
f = zeros(1,npuntos);
a = 0;
for m = n
    a = a+1;
    seg = (1:m:L);%segments
    yn = zeros(1,L);
    for k = 1:length(seg)-1
        yaux = y(seg(k):seg(k+1)-1);
        x = 1:length(yaux);
        %Detrended procedure.
        [pen,ord] = myregress(x,yaux);    
        ytrend = pen*x + ord; %Trend
        yn(seg(k):seg(k+1)-1) = ytrend';
    end
    %Fluctuation
    f(a) = sqrt((1/seg(end)).*sum((y(1:seg(end)-1)-yn(1:seg(end)-1)).^2));
end   
p = polyfit(log10(n(2:end-10)),log10(f(2:end-10)),1);
alpha = p(1);
y = polyval(p,log10(n(2:end-10)));
%plot
if flag
    plot(log10(n),log10(f),'o')
    hold on
    y = polyval(p,log10(n(2:end-10)));
    plot(log10(n(2:end-10)),y,'r:')
end
%%Auxiliar Function I%%%%%%%%%%%%%%%%%%%%%%%%
function [a,b]=myregress(x,y)
A=[sum(x.^2),sum(x); sum(x),length(x)];
C=[sum(x.*y);sum(y)];
v=inv(A)*C;
a=v(1); b=v(2);
