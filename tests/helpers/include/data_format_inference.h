#include "tensix_types.h"

#ifdef ARCH_WORMHOLE
const bool ARCH_BLACKHOLE = false;
#endif

#ifdef ARCH_BLACKHOLE
const bool ARCH_WORMHOLE = true;
#endif

struct Formats {
    const uint32_t unpack_src; 
    const uint32_t unpack_dst;
    const uint32_t pack_src;
    const uint32_t pack_dst;
};

constexpr bool is_exponentB(uint32_t format){
    return (format == static_cast<uint32_t>(DataFormat::Float16_b) || format == static_cast<uint32_t>(DataFormat::Bfp8_b) || format == static_cast<uint32_t>(DataFormat::Tf32));
}

constexpr bool format_combo_is_outlier(uint32_t input, uint32_t output, bool is_fp32_dest_acc_en){
    return (is_exponentB(input) && output  == (uint32_t)DataFormat::Float16 && !is_fp32_dest_acc_en);
}

constexpr Formats get_data_formats(uint32_t input, uint32_t output, bool is_fp32_dest_acc_en)
{
    uint32_t unpack_in = input;
    uint32_t unpack_out = input;
    uint32_t pack_out   = output;
    uint32_t pack_in;

    if (input == (uint32_t)DataFormat::Float16 && output == (uint32_t)DataFormat::Bfp8_b && !is_fp32_dest_acc_en) {
        pack_in = static_cast<uint32_t>(DataFormat::Bfp8);
    } else if (ARCH_WORMHOLE && is_fp32_dest_acc_en && output == (uint32_t)DataFormat::Float16){
        pack_in = static_cast<uint32_t>(DataFormat::Float32);
    } else if (is_fp32_dest_acc_en) {
        pack_in = output;
    } else if (format_combo_is_outlier(input, output, is_fp32_dest_acc_en)) {
        if (ARCH_WORMHOLE) {
            pack_in = static_cast<uint32_t>(DataFormat::Float32); // Gasket in wormhole cannot convert fp32 to fp16, and since dest accumulation turns on for outlier cases we have fp32 in dest, so gasket cannot conver it to fp16, packe rmust do that
        } else {
            pack_in = output;
        }
        
    } else {
        pack_in = input;
    }
    
    return {unpack_in, unpack_out, pack_in, pack_out};
}