# glibc

```bash
wget http://ftp.gnu.org/gnu/glibc/glibc-2.34.tar.gz
tar -xzf glibc-2.34.tar.gz
cd glibc-2.34
mkdir build && cd build
../configure --prefix=/opt/glibc-2.34  # Specify the install path
make -j$(nproc) && sudo make install
```
