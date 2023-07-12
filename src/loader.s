global loader                   ;the entry symbol for ELF / ELF 的入口符号

MAGIC_NUMBER equ 0x1BADB002     ; define the magic number constant / 定义幻数常量
FLAGS        equ 0x0            ; multiboot flags / 多重引导标志
CHECKSUM     equ -MAGIC_NUMBER  ; calculate the checksum / 计算校验和
                                ; (magic number + checksum + flags should equal 0)
                                ; （幻数 + 校验和 + 标志应等于 0）
section .text:                  ; start of the text (code) section / 文本（代码）部分的开头
align 4                         ; the code must be 4 byte aligned / 代码必须为 4 字节对齐
    dd MAGIC_NUMBER             ; write the magic number to the machine code, / 将幻数写入机器代码，
    dd FLAGS                    ; the flags, / 旗帜，(机翻经典QWQ)
    dd CHECKSUM                 ; and the checksum / 和校验和
loader:                         ; the loader label (defined as entry point in linker script) / 加载程序标签（在链接器脚本中定义为入口点）
    mov eax, 0xCAFEBABE         ; place the number 0xCAFEBABE in the register eax / 将0xCAFEBABE的数字放入寄存器 EAX 中
.loop:
    jmp .loop                   ; loop forever / 永远循环
