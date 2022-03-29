photolist = dir('./PhotoMatte85/*.png');
backgroundlist = dir('./Backgrounds/*.jpg');

mkdir dataset
mkdir dataset/lable
mkdir dataset/live

% fid = fopen( 'dataset\filelist.txt', 'W' );
for i=1:length(photolist)
    
    importpngfile(fullfile(photolist(i).folder,photolist(i).name));

    [w,h] = size(alpha);
    s = min(w,h);
    q_alpha = alpha(1:s, 1:s, :);
    q_cdata = cdata(1:s, 1:s, :);

%     j = 1;
    parfor j=1:length(backgroundlist)
        back_image = imread(fullfile(backgroundlist(j).folder,backgroundlist(j).name));
        [bw,bh,~] = size(back_image);
        bs = min(bw,bh);
        q_back = back_image(1:bs, 1:bs, :);
    
        q_rsback = imresize(q_back, [s, s]);
        q_rsaback = imresize(q_back, [s, s]).* (1- q_alpha/255);
        q_acdata = q_cdata.* (q_alpha/255);
        q_add_data = q_rsaback + q_acdata;
    
        s_data  = imresize(q_add_data, [512, 512]);
        s_alpha = imresize(q_alpha, [512, 512]);
    
        s_data_path = ['dataset\live\live_',num2str(1000*i+j),'.png'];
        s_alpha_path = ['dataset\lable\lable_',num2str(1000*i+j),'.png'];
%         s_data_path = ['dataset\live\my_',num2str(1000*i+j),'_leftImg8bit.png'];
%         s_alpha_path = ['dataset\lable\my_',num2str(1000*i+j),'_gtFine_labelIds.png'];
        imwrite(s_data, s_data_path)
%         imwrite(s_alpha, ['dataset\lable\lable_',num2str(1000*i+j),'.png'])
        imwrite(logical(s_alpha/200), s_alpha_path)

%         fwrite( fid, [s_data_path,' ', s_alpha_path]);
%         fwrite( fid,"\r\n");
    end
end
% fclose(fid);