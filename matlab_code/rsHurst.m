function [H] = rsHurst(rr,flag)
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% Hurst exponent estimated by the RS method.
%
%
% USE:
%	[H] = rsHurst(rr,flag)
%
% INPUT: 
%       .-rr ---> Time series
%       .-flag ---> Plot (flag=1) the estimate procedure.
% ...DE  SALIDA: 
%       .-H ---> Parámetro de Hurst estimado.
%
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% AUTHORS:
% OSCAR BARQUERO PEREZ
% Rebeca Goya Esteban
% 
% DATE: 28-09-2007
%
% VERSION 1.0

rr = diff(rr); %First compute the fGn = diff(fBm).
maxPot2 = 2.^floor(log2(length(rr)));
datosAux = rr(1:maxPot2);
tamCaja = maxPot2;
numIter = 1;
RSave = [];
cajas = 1;
tC = [tamCaja];
while (tamCaja >= 8)
    inds = [];
    m = 1;
    for l = 1:cajas %Index for this segment lenght
        indsaux = (m : m+tamCaja-1) ;
        m = m + tamCaja;
        inds = [inds; indsaux];   
    end
    
    RSiter = [];
    for g = 1:size(inds,1) %RS compute for this segment length
        RSaux = RScalc(datosAux(inds(g,:)));
        RSiter = [RSiter; RSaux];    
    end
    RSave = [RSave;mean(RSiter)];    
    numIter = numIter + 1;
    tamCaja = tamCaja / 2;
    cajas = 2.^(numIter-1);
    tC = [tC;tamCaja];
end
tC = tC(1:end-1);

[H, rectaReg, barrasError] = myregress(tC(end-1:-1:1),RSave(end-1:-1:1),flag);

%%Auxiliar Functions I%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [H, rectaReg, barrasError] = myregress(tC,RSave,plotFlag)
x = [ones(length(tC),1) log2(tC)];
y = log2(RSave);
[c,cint,r,rint,stats] = regress(y,x,0.05);
rectaReg = x*c;
barrasError = abs(rint(:,1)-r);
H = abs(c(2));

%Plot
if plotFlag
    plot(log2(tC),y,'o-')
    hold on
    plot(log2(tC),rectaReg,'r--');
end

%%Auxiliar Functions II%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function RS = RScalc(rr)
%RS compute
N = length(rr);
mediaDatos = sum(rr)/N; %Data mean
X = cumsum(rr-mediaDatos);
R = max(X) - min(X); %Range
S = sqrt(sum((rr-mediaDatos).^2)/N); %STD
RS = R/S; %RS 

