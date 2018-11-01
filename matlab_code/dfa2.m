function [alpha1,alpha2] = dfa2(rr,a2_up_scale,flag)
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% DFA scaling exponents alpha1 and alpha2 estimate.
%
% USE:
%	[alpha1,alpha2] = dfa(rr,flag)
%
% USE:
%	[alpha] = dfa(rr,flag)
%
% INPUT: 
%       .-rr ---> Time series.
%       .-flag ---> Plot (flag=1) the estimate procedure.
% OUTPUT: 
%       .-alpha1 ---> Scaling exponent short-term. 4-16 beats
%       .-alpha2 ---> Scaling exponent long-term. 16-64 beats
%        
%""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
% AUTHORS:
% REBECA GOYA ESTEBAN
% OSCAR BARQUERO PEREZ
% 
% DATE: 18-10-2007
%
% VERSION 1.0
rr = rr(:);
if nargin<2
    flag = 0;
    a2_up_scale = 64;
end
rr = rr - mean(rr);
y = cumsum(rr);
L = length(y);

%box creation
rs = box_creation(L);

npuntos = length(rs);
F = zeros(1,npuntos);

for m = 1:npuntos
   
    num_seg = floor(L / rs(m));
    yn = zeros(1,floor(num_seg*rs(m)));
    
    for k = 1:num_seg
        yaux = y( (k-1)*rs(m)+1:k*rs(m) );
        x = 1:length(yaux);
        
        %Detrended procedure.
        [pen,ord] = myregress(x',yaux);    
        ytrend = pen*x + ord; %Trend
        yn((k-1)*rs(m)+1:k*rs(m)) = ytrend';
    end
    
    %Fluctuation
    N = length(yn);
    F(m) = sqrt((1/length(yn)).*sum((y(1:N)-yn(1:N)').^2));
    
end  


ind_alpha1 = (4 <= rs & rs <= 16);
ind_alpha2 = (16 <= rs & rs <= 64);

p1 = polyfit(log10(rs(ind_alpha1)),log10(F(ind_alpha1)'),1);
alpha1 = p1(1);
p2 = polyfit(log10(rs(ind_alpha2)),log10(F(ind_alpha2)'),1);
alpha2 = p2(1);

y = polyval(p1,log10(rs(ind_alpha1)));
y1 = polyval(p2,log10(rs(ind_alpha2)));


%Plot
if flag
    plot(log10(rs(ind_alpha1)),log10(F(ind_alpha1)),'^')
    hold on
    plot(log10(rs(ind_alpha2)),log10(F(ind_alpha2)),'^')
    plot(log10(rs(ind_alpha1)),y,'r-')
    plot(log10(rs(ind_alpha2)),y1,'r-')
end

end
%%Auxiliar FunctionI%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [a,b]=myregress(x,y)
A=[sum(x.^2),sum(x); sum(x),length(x)];
C=[sum(x.*y);sum(y)];
v=inv(A)*C;
a=v(1); b=v(2);
end


function n = box_creation(L)
%%Function that creates the box of n for dfa analysis

min_box = 4;
max_box = L / 4;
box_ratio = 2^(1/8);

num_scales = floor(log10(max_box/min_box) / log10(box_ratio) + 1.5);

n = zeros(num_scales,1);

n(1) = min_box;

k = 2;
ir = 1;

while (k <= num_scales && n(k-1) < max_box)
    rw = floor(min_box * box_ratio^ir + 0.5);
    if (rw > n(k-1))
        n(k) = rw;
    end
    k = k+1;
    ir = ir +1;
end

n(n==0) = []; %remove box with zero

end