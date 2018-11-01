function  res = aci(rr)
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% PROPÓSITO:
%  Funcion que recibe como parametro una serie temporal y calcula el indice
% ACI (Acceleration Change Index) que caracteriza el signo de las
% diferencias de las series temporales
%
% FORMA DE USO:
%	[res] = aci(rr);
%
% ARGUMENTOS...
% ...DE ENTRADA: 
%       .-rr ---> Serie temporal, serie de
%       intervalos NN de 24hh.
% ...DE  SALIDA: 
%       .-res  --->  indice ACI de la serie temporal.
%
% COMENTARIOS:
%
%
% VER TAMBIÉN:
%   See also	
%
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% AUTORES: 
% OSCAR BARQUERO PEREZ
% REBECA GOYA ESTEBAN
% 
% FECHA: 03-11-2007
%
% VERSION 1.1
%
% BIBLIOGRAFIA:
%  .- García-González, M. A., J. Ramón-Castro, et al. (2003). "A new index
% for the analysis of heart rate variability dynamics: characterization and 
% application." Physiological measurement 24: 819-832.
%
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
%
%


%paso 1: diferenciacion de las series RR

DRR = diff(rr);

%paso 2: obtener signo de DRR

%Por problemas con la fluctuación en el redondeo del mapa logistico,
%colocamos eps

SDRR = zeros(length(DRR),1);
%Para los DRR >= 0
ind = find(DRR>=0);
SDRR(ind) = 1;


% SDRR = sign(DRR+eps);
% indiceA = find(SDRR == 0);
% indiceB = find(SDRR == -1);
%SDRR(indiceA)=1;
%SDRR(indiceB)=0;
                                                         
%paso 3: obtener cambios de signo 

SC=find(SDRR(1:end-1) ~= SDRR(2:end))+1;

if isempty(SC)
    SC = 0;
end


%paso 4: diferenciacion de SC para obtener la distancia (en latidos) entre
%sucesivos cambios de signo de la serie temporal DRR.

DSC = diff(SC);

if isempty(DSC)
    DSC = 0;
end

%calculo ACI

k = length(find(DSC == 1));
M = length(DSC);
res = k / M;
