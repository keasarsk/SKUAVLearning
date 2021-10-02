# Dronekit-configure-in-unbuntu
Unbuntu + dronekit-SITL + MAVProxy + MissionPlanner

学习记录

# 通 #

##  MAVLink  ##
- 是在串口通讯基础上的一种更高层的开源**通讯协议**，主要应用在微型飞行器的通讯上。为小型飞行器和地面站通讯时常用数据制定了一种发送和接受的规则，并加入了校验功能。协议以消息库的形式定义了参数传输的规则。
- 是一个为微型飞行器设计的非常轻巧的、只由头文件构成的信息编组库。它可以通过串口非常高效地封装C结构数据，并将这些数据包发送至地面控制站。该协议被PX4, PIXHAWK, APM和Parrot AR.Drone平台所广泛测试并在以上的项目中作为MCU/IMU间以及Linux进程和地面站链路通信间的主干通信协议。

##  Dronekit-Python  ##
- 一个用于控制无人机的Python 库，提供了用于无人机的**API**，其代码独立于飞控，单独运行在机载电脑或其他设备上，通过串口或无线的方式经 *MAVLink* 协议与飞控板通信。  
- 对于Dronekit，PX4被支持的较少，不可以进行模式切换，而对Ardupilot支持的比较多，可调用的函数也比较多。
##  MAVSDK-Python  
[MAVSDK-Python](https://auterion.com/getting-started-with-mavsdk-python/)
	    
- MAVSDK是各种编程语言库的集合，用于与无人机、相机或地面系统等MAVLink系统进行交互。
- 这些库提供了一个简单的 **API**，用于管理一辆或多辆车辆，提供对车辆信息和遥测的编程访问，
- 以及对任务、移动和其他操作的控制。
- 这些库可以在无人机上的配套计算机上使用，也可以在地面站或移动设备上使用。
- MAVSDK 是跨平台的：Linux、macOS、Windows、Android 和 iOS。

##  SITL  
[SITL](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html)
	
- SITL 模拟器允许您在没有任何硬件的情况下运行 Plane、Copter 或 Rover。它是使用普通 C++ 编译器构建的自动驾驶仪代码，为您提供本机可执行文件，允许您在没有硬件的情况下测试代码的行为。
- SITL 在 Linux 和 Windows 上本地运行。
##  dronekit-SITL ##
- 开源软件模拟器
- 用户可以在不依托任何硬件的情况下，对固定翼(Plane)、旋翼机(Copter)和车辆(Rover)进行模拟。除了进行路径规划测试、参数设置测试、控制代码调试以外，SITL还可模拟风力、地形等外部环境，安装模拟光流、激光雷达等传感器，与其他设备通过串口、网络通信等等。
##  MAVProxy ##
[MAVProxy](https://ardupilot.org/mavproxy/index.html#home)
	
- 数据转发软件,基于 MAVLink 的系统的无人机地面站软件包
- MAVProxy 是一款用于无人机的全功能 GCS，设计为一款简约、便携和可扩展的 GCS，适用于任何支持 MAVLink 协议的自主系统（例如使用 ArduPilot 的系统）。MAVProxy 是一个功能强大的基于命令行的“开发者”地面站软件。它可以通过附加模块进行扩展，或与另一个地面站（例如 Mission Planner、APM Planner 2、QGroundControl 等）相辅相成，以提供图形用户界面。
- 为了充分利用 SITL，您确实需要学习使用 MAVProxy
##  Gazebo  
[Gazebo](https://docs.px4.io/master/en/simulation/gazebo.html)
		
- 是一个强大的自主机器人 3D 仿真环境，特别适用于测试物体回避和计算机视觉。此页面描述了它与 SITL 和单个车辆的使用。Gazebo 还可以与HITL一起使用并用于多车辆模拟。  
- 构建机器、场景、传感器、物理性质等的 模型

##	QGC-QGroundControl
[QGC-QGroundControl](https://docs.qgroundcontrol.com/master/en/index.html)  
- QGroundControl为 PX4 或 ArduPilot 动力车辆提供完整的飞行控制和车辆设置

##  aioconsole  
- 轻量级软件包。这提供了一个 REPL（交互式 shell）apython，我们可以使用它来运行 asyncio 代码 
## ArduPilot 
[ArduPilot](https://ardupilot.org/dev/index.html )
	 
ArduPilot是领先的开源自动驾驶系统，支持多旋翼、传统直升机、固定翼飞机、漫游者、潜艇和天线跟踪器。  

	飞机 - 飞机的自动驾驶仪
	Copter  - 多旋翼机和传统直升机的自动驾驶仪
	Rover  - 地面车辆的自动驾驶仪
	Sub  - 潜水器的自动驾驶仪

	Antenna Tracker  - 用于自动将天线对准车辆
	Mission Planner  - 最常用的地面站，用 C# 为 windows 编写，但也可以通过 mono 在 Linux 和 MacOS 上运行
	APM Planner 2.0  是一个专门为 APM 使用 Qt 库用 C++ 编写的地面站
	MAVProxy - 面向命令行且可编写脚本的地面站（主要由开发人员使用）

	DroneKit - 用于在车辆、移动设备和/或云中运行的应用程序的 APM SDK。
	MinimOSD  - 飞行数据的屏幕显示
	Tower  - 安卓地面站
	QGroundControl*是使用 Qt 库以 C++ 编写的替代地面站
	PX4* - 原始 PX4FMU 硬件（Pixhawk 的开发者）的设计者
	MAVLink* - 地面站、飞行控制器和一些外围设备（包括 OSD）之间的通信协议。使用 MAVLink 的“虚拟指南”在 这里。
	UAVCAN* - 轻量级协议，旨在通过 CAN 总线在航空航天和机器人应用中进行可靠通信。ArduPilot 正在使用Libuavcan，这是一个用 C++ 编写的可移植的跨平台库，对 C++ 标准库的依赖最小。


## PX4
[PX4](https://docs.px4.cc/master/zh/getting_started/px4_basic_concepts.html)  
PX4 is powerful open source autopilot flight stack.  
PX4是一个广泛的无人机平台的核心部分，该平台包括QGroundControl地面站、Pixhawk硬件和MAVSDK，用于与使用MAVLink协议的配套计算机、摄像机和其他硬件集成。PX4由droncode项目支持  
  
[PX4系统架构概述](https://dev.px4.cc/master/zh/concept/architecture.html)  

## PX4与ArduPilot对比 ##
[PX4与ArduPilot对比](https://blog.csdn.net/lixiaoweimashixiao/article/details/81545640?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162755779116780366560732%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=162755779116780366560732&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_v29-2-81545640.pc_v2_rank_blog_default&utm_term=ArduPilot%E4%B8%8Epx&spm=1018.2226.3001.4450)

## WAF ##
[waf](https://waf.io/book/)  




## ROS-kinetic ##
[ROS](https://zhuanlan.zhihu.com/p/64502836 )  是一个适用于机器人的开源的元操作系统。其实它并不是一个真正的操作系统，其底层的任务调度、编译、寻址等任务还是由Linux操作系统完成，也就是说ROS实际上是运行在Linux上的次级操作系统。  

一个版本ubuntu对应一个ROS版本  
ubuntu对应ROS-Melodic




# ------------------------------------------------------- #
# python2 
# dronekit
# dronekit-sitl
# mavproxy
# MissionPlanner
# 模拟仿真 #

##  .MissionPlanner  
- 是用于 ArduPilot 开源自动驾驶仪项目的全功能地面站应用程序


#   配置步骤   #
## 1.在unbuntu中安装python2(dronekit包不支持python3)  
bash中：  

    sudo apt install python

## 2.安装dronekit、dronekit-sitl、mavproxy 
bash中：

	pip install dronekit
	pip install dronekit-sitl
	pip install mavproxy
- 注：此步骤可能出现的错误 pip命令无法识别，则，安装pip命令  
bash中：

	sudo apt install python-pip

## 3.启动dronekit-sitl，并配置home点、机型 
bash中：

	dronekit-sitl  copter --home=39.9,116.38,3,30 --model=quad

- --home=纬度，经度，3,30 经纬度可自行设置  

## 4.启动mavproxy数据转发服务 
另开一个bash窗口，cd到mavproxy.py文件目录：

	cd ~/.local/bin/
	python mavproxy.py  --master=tcp:127.0.0.1:5760  --out=***missionPlanner电脑的IP:自拟端口号***  --out=127.0.0.1:14550 

- tcp:127.0.0.1:5760： SITL默认端口，作为mavproxy的输入，把输入数据转发到如下两个端口  
- 127.0.0.1:14550 ： 本机地址14550端口，供本地python程序连接(此端口号对应py程序中连接端口号)   
- *missionPlanner电脑的IP:自拟端口号*：同一局域网内另一台电脑地址(若unbuntu运行在虚拟机中，此处可在Windows本机IP)，供MissionPlanner连接    

python mavproxy.py  --master=tcp:127.0.0.1:5760  --out=172.20.10.2:55555  --out=127.0.0.1:14550 

## 5.启动MissionPlanner 
- 右上角选择UDP连接，端口号填写步骤4中自拟端口号  
- 注：此步骤可能出现地图无法加载，则  
- 左上角***飞行计划***->右侧地图选项选择高德(或其他)

## 6.运行dronekit程序 .py文件  
再另新开一个bash：  
	cd .py文件目录
	python 文件名.py  

- 此步将在MissionPlanner中看到你得dronekit程序控制的无人机运行状况。

# ------------------------------------------------------- #
# Python3  
# MAVSDK
# SITL
# mavproxy
# MAVSDK入门  

## 安装MAVSDK-Python ##
安装 MAVSDK-Python

	sudo apt install python3-pip  
	pip3 install --user mavsdk

##  安装aioconsole  

可以快速检验
为了快速启动 REPL（交互式 shell），我们还将安装名为“aioconsole”的轻量级包，它提供apython（用于运行异步代码的 REPL）    
	
	pip3 install aioconsole  

##  设置ArduPilot的ubuntu环境 包括SITL
[设置ArduPilot的ubuntu环境](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html)
	
：

	sudo apt-get update
	sudo apt-get install git
	sudo apt-get install gitk git-gui

	git clone https://github.com/ArduPilot/ardupilot.git  建议↓  
	git clone --recursive https://github.com/ArduPilot/ardupilot.git
	cd ardupilot  
	git submodule update --init --recursive #出错几次后再运行无反应了 继续↓  
Tools/environment_install/install-prereqs-ubuntu.sh -y  # 失败   

	~/.profile  
##  waf构建ardupolit  
[waf构建ardupolit](https://github.com/ArduPilot/ardupilot/blob/master/BUILD.md)
	  

	 cd ardupilot
未进行

## 启动SITL ##

	cd ~/ardupilot/ArduCopter
	将   /home/keasar/ardupilot/Tools/autotest/sim_vehicle.py 文件拖入终端
	第一次： sim_vehicle.py -w  成功
	        ctrl + c 结束第一次运行
	sim_vehicle.py --console (控制台) --map -v ArduCopter -L home 
- map加载失败  
	原因未在python3中配置mavproxy：  
  	配置python3环境  
	sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-lxml python3-pygame  
	安装一些python3的包 其中python3-pygame不可用 ，命令行中可减去

	pip3 install PyYAML mavproxy --user python3安装MAVProxy  
	echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc  
	pip3 install mavproxy --user --upgrade  更新mavproxy
- 更改map源   
	在map界面 view - server 选中后 再去/home/keasar/ardupilot/Tools/autotest中改：请将以下几行添加到“.bashrc”的末尾（将 MicrosoftHyb 更改为所需的提供程序）：  
	export MAP_SERVICE="地图名字"
- home的设置：  
	ardupilot\Tools\autotest其中的locations.txt文件末尾添加home或其他位置并设置名字
- SITL更多使用： 
- [] (https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html#using-sitl-for-ardupilot-testing)
	

## 运行mavproxy  
[运行mavproxy](https://ardupilot.org/mavproxy/docs/getting_started/quickstart.html)
	
方法同python2，：
	cd ~/.local/bin/
	python3 mavproxy.py  --master=tcp:127.0.0.1:5760  --out=172.20.10.2:55555  --out=127.0.0.1:14550
然后启动SITL 就可以看见map。
可能需要修改mavproxy.py的首行 

## apython
	from mavsdk import System
	drone = System()
	await drone.connect()
此时 Connected to mavsdk_server!  
然后执行  
await drone.action.arm()
await drone.action.takeoff()  
时出错误   
原因可能是未配置PX4






# ------------------------------------------------------- #
## 草稿，待整理 ##

安装需要的依赖  
	
	sudo apt-get install python-dev python3-dev libxml2-dev libxslt1-dev zlib1g-dev
	git clone https://github.com/dronekit/dronekit-python.git
	cd ./dronekit-python
	sudo python setup.py build
	sudo python setup.py install
## [固件 firmware](https://baike.baidu.com/item/%E5%9B%BA%E4%BB%B6) ##
固件是指设备内部保存的设备“驱动程序”，通过固件，操作系统才能按照标准的设备驱动实现特定机器的运行动作
## nuttx ##
Nuttx 是一个实时嵌入式操作系统（Embedded RTOS），它很小巧，在微控制器环境中使用。Nuttx完全可扩展，可从从小型（8位）至中型嵌入式（32位）系统。它的设计目的还在于完全符合POSIX标准，完全实时，并完全开放。
# ------------------------------------------------------- #

# Ubuntu18.04下安装ROS

[melodic官网步骤](http://wiki.ros.org/melodic/Installation/Ubuntu)   

	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'  
	sudo apt install curl   

	curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
    此步骤失败 替换为 翻墙登录该网址 复制证书至ubuntu中命名为ros.asc后在该目录下执行 sudo apt-key add ros.asc  

	sudo apt install ros-melodic-desktop-full
	此步骤失败 使用aptitude进行安装，aptitude 会对依赖关系进行智能处理 替换为：  
	sudo apt-get install aptitude
	sudo aptitude install ros-melodic-desktop-full


# -------------------------8.4 翻墙------------------------------ #
网址 china.tg   
	shadowsocksR 

# -------------------------8.5 PX4开发环境------------------- #

[linux环境配置](https://docs.px4.io/master/en/dev_setup/dev_env_linux_ubuntu.html#rosgazebo)  

	git clone https://github.com/PX4/PX4-Autopilot.git --recursive  
	此步在win E盘