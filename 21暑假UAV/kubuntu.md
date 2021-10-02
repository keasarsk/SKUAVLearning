#  8.8kubuntu重装  
##  shadowsockets  
[节点](china.TG)    
订阅地址：https://j04.space/link/Pp8LnIleTlrmSChU  

- E盘里.AppImage 文件直接拖过去 双击 
- 安装electron-ssr 然后左下角添加订阅地址
- 然后右上角绿飞机 先更新PAC 、然后选择服务器地址、然后改代理模式

无法访问 安装依赖：  
https://github.com/qingshuisiyuan/electron-ssr-backup/blob/master/Ubuntu.md  

	sudo apt install libcanberra-gtk-module libcanberra-gtk3-module gconf2 gconf-service libappindicator1  

	sudo apt install python

全局代理 好了。 原因可能是python和依赖未安装
##  PX

	sudo apt install git
Gazebo、JMAVSim 和 NuttX (Pixhawk)  

	bash ./PX4-Autopilot/Tools/setup/ubuntu.sh

“无法获得锁”解决方案(E: 无法获得锁 某目录  
rm 该lock文件  

##  树莓派  
	wget https://raw.githubusercontent.com/PX4/PX4-Autopilot/master/Tools/setup/ubuntu.sh  
无法建立 SSL 连接  
wget "http://www.indeed.com/" --user-agent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
给root用户设置密码：
命令：sudo passwd root  
退出 vim 编辑 :q  :q!  
wget成功 操作包括 开小飞机 加hosts URL加""  

	wget https://raw.githubusercontent.com/PX4/PX4-Autopilot/master/Tools/setup/requirements.txt  
	bash ubuntu.sh --no-nuttx --no-sim-tools

sudo apt-get install -y gcc-8-arm-linux-gnueabihf g++-8-arm-linux-gnueabihf

sudo apt-get install -y gcc-8-aarch64-linux-gnu g++-8-aarch64-linux-gnu

sudo apt-get install clang

wget https://raw.githubusercontent.com/PX4/Devguide/master/build_scripts/ubuntu_sim_ros_melodic.sh
wget基本是网络问题 多试几次   

bash ubuntu_sim_ros_melodic.sh  
无法获得锁/var/lib/dpkg  
sudo rm /var/lib/dpkg/lock-frontend  
sudo rm /var/lib/dpkg/lock
完成  

# 快速DDS安装  
	https://docs.px4.io/master/en/dev_setup/fast-dds-installation.html  

##java

##gradle

##sdkman
	https://sdkman.io/install

##sdk install gradle 7.1.1  

##Foonathan Memory 依赖项    （失败）
git clone https://github.com/eProsima/foonathan_memory_vendor.git

sudo cmake --build . --target install
失败：ssl建立连接失败  
解决：调试小飞机 多试几遍 失败  

升级curl  
	https://blog.csdn.net/bloodfeast/article/details/77824713?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163016010316780366580123%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=163016010316780366580123&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~hot_rank-1-77824713.pc_search_result_cache&utm_term=ubuntu%E5%8D%87%E7%BA%A7curl&spm=1018.2226.3001.4187  
失败  

