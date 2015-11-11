% Function to find next minimum point

function [storage] = find_min(start, vector,storage)
    %display('now finding min')
    endV = start;

    while (endV ~= length(vector) && min(vector(start:endV)) ~= min(vector(start:endV + 1)))
        endV = endV + 1;
    end
    
    if (endV ~= length(vector))
        index = length(storage) + 1;
        storage(index,1) = vector(endV);
        storage(index,2) = endV;
        storage = find_max(endV,vector,storage);
        return
    else
        return
    end
    
end