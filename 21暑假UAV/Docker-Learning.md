#Docker  
[Docker](https://www.topgoer.cn/docs/docker/docker-1cbqgmmc4pf24)  
容器是一种虚拟化的方案，和传统的虚拟机(通过中间层”guerst OS”运行服务)不同，Docker直接运行在操作系统之上。因此容器虚拟化也被称之为操作系统虚拟化。Docker容器依赖于Linux内核特性，Namespace和Cgroups，所以只能运行在Linux之上。
一句话来概括的话，主机级虚拟化（比如VMware）就是通过各种各样的手段，把物理资源重新分配，然后抽象出一部分拿来做虚拟机的虚拟硬件，是对硬件的模拟；而容器虚拟化技术相当于把操作系统进行虚拟化，把物理的操作系统模拟为逻辑上的多个操作系统，不同的操作系统有自己的用户空间，实现了应用程序间的隔离。  

![](https://www.topgoer.cn/uploads/docker/images/m_a17f22754b509dc36a8307fc7153dde1_r.png)  
![](https://www.topgoer.cn/uploads/docker/images/m_19c07eada4f465e385e4d1d9648bf6f6_r.png)