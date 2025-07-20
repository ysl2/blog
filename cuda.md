# cuda

## Linux 内核版本更新导致nvidia驱动挂了

> 场景：运行`nvidia-smi`命令的时候，报错：NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.

原因：缺少当前内核的头文件，这通常发生在内核更新之后。

```bash
sudo apt install linux-headers-"$(uname -r)"
```

> Ref: <https://zhuanlan.zhihu.com/p/89714824>

```bash
sudo apt install dkms
# 下面这条命令有可能报错找不到`linux-headers-xxxx-amd64`。此时需要通过apt安装一下。
sudo dkms install -m nvidia -v 418.87.00
```

其中，418.87.00 是之前安装 nvidia 驱动的版本号，可通过下面方法查到：

```bash
# 如果下面这条命令显示的是`nvidia-current-418.87.00`，那还需要将其软连接到`/usr/src/nvidia-418.87.00`
ls /usr/src | grep nvidia
```

## 没有进程，但是显存有占用

用以下命令查看所有在显卡上运行的进程。

**注意: 这种方法会打印所有卡上的进程，因此一旦kill，所有卡的都会停，非常危险，需要谨慎使用**

```bash
fuser -v /dev/nvidia*
```
