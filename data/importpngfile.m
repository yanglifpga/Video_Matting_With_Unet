function importpngfile(fileToRead1)
%IMPORTFILE(FILETOREAD1)
%  从指定文件中导入数据
%  FILETOREAD1:  要读取的文件

%  由 MATLAB 于 27-Mar-2022 11:23:47 自动生成

% 导入文件
newData1 = importdata(fileToRead1);

% 在基础工作区中从这些字段创建新变量。
vars = fieldnames(newData1);
for i = 1:length(vars)
    assignin('base', vars{i}, newData1.(vars{i}));
end

