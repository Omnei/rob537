% Function to find next minimum point

function [storage] = find_max(start, vector, storage)
    %display('now finding max');
    endV = start;

    while (endV ~= length(vector) && max(vector(start:endV)) ~= max(vector(start:endV + 1)))
        endV = endV + 1;
    end
    
    if (endV ~= length(vector))
        index = length(storage) + 1;
        storage(index,1) = vector(endV);
        storage(index,2) = endV;
        storage = find_min(endV,vector,storage);
        return
    else
        return
    end
    
end